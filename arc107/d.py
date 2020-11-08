# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve_TLE(N, K):
    MOD = 998_244_353
    table = [[-1] * (N + 1) for _i in range(N + 1)]
    table[0] = [0] * (N + 1)
    table[0][0] = 1
    table[1] = [0] * (N + 1)
    table[1][1] = 1
    # for i in range(12):
    #     if i >= N:
    #         break
    #     table[1][i] = 1

    def f(k, n):
        # debug(k, n, msg=":k, n")
        try:
            v = table[n][k]
        except:
            debug(k, n, msg=":k, n")
            raise
        if v != -1:
            return v
        if k > n:
            table[n][k] = 0
            return 0
        debug(k, n, msg=":k, n")
        # if n == 0:
        #     if k == 0:
        #         return 1
        #     return 0
        if k <= 0:
            table[n][k] = 0
            return 0
        if n == k:
            table[n][k] = 1
            return 1

        ret = 0
        for x in range(n + 1):
            new_k = 2 * (k - x)
            if new_k > N:
                continue
            if new_k < 0:
                break
            ret += f(new_k, n - x)
        table[n][k] = ret % MOD
        return ret

    ret = f(K, N)
    # debug(table, msg=":table")
    return ret


def solve(N, K):
    MOD = 998_244_353
    table = [[-1] * (N + 1) for _i in range(N + 1)]
    table[0] = [0] * (N + 1)
    table[0][0] = 1
    table[1] = [0] * (N + 1)
    table[1][1] = 1

    def f(k, n):
        # debug(k, n, msg=":k, n")
        if k > N:
            return 0
        try:
            v = table[n][k]
        except:
            debug(k, n, msg=":k, n")
            raise
        if v != -1:
            return v
        if k > n:
            table[n][k] = 0
            return 0
        # debug(k, n, msg=":k, n")
        if k <= 0:
            table[n][k] = 0
            return 0
        if n == k:
            table[n][k] = 1
            return 1

        ret = f(k - 1, n - 1)
        ret += f(2 * k, n)
        ret %= MOD
        table[n][k] = ret
        return ret

    ret = f(K, N)
    # debug(table, msg=":table")
    return ret


def main():
    # parse input
    N, K = map(int, input().split())
    print(solve(N, K))


# tests
T1 = """
4 2
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
2
"""

T2 = """
2525 425
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
687232272
"""

T3 = """
8 2
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
16
"""


def _test():
    import doctest
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
            print(k)
            doctest.run_docstring_examples(g[k], g, name=k)


def as_input(s):
    "use in test, use given string as input file"
    import io
    f = io.StringIO(s.strip())
    g = globals()
    g["input"] = lambda: bytes(f.readline(), "ascii")
    g["read"] = lambda: bytes(f.read(), "ascii")


if __name__ == "__main__":
    import sys
    input = sys.stdin.buffer.readline
    read = sys.stdin.buffer.read
    sys.setrecursionlimit(10 ** 6)
    if sys.argv[-1] == "-t":
        print("testing")
        _test()
        sys.exit()
    main()
    sys.exit()

# end of snippets/main.py
