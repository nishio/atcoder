# included from snippets/main.py
from sys import dont_write_bytecode


def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(X, AS):
    from collections import defaultdict
    INF = 9223372036854775807
    N = len(AS)

    def to_key(mod, num):
        return num * (k + 1) + mod

    def from_key(key):
        num, mod = divmod(key, k + 1)
        return (mod, num)

    sumAS = sum(AS)
    ret = INF
    for k in range(N, 0, -1):
        if (X - sumAS) // k > ret:
            break
        SIZE = (k + 1) ** 2
        table = [-1] * SIZE
        table[to_key(0, 0)] = 0

        for a in AS:
            for key in reversed(range(SIZE)):
                if table[key] == -1:
                    continue
                mod, num = from_key(key)
                v = table[key] + a
                num += 1
                if num > k:
                    continue
                mod = v % k
                key = to_key(mod, num)
                table[key] = max(table[key], v)

        for key in range(SIZE):
            if table[key] == -1:
                continue
            mod, num = from_key(key)
            if num == k and num > 0:
                v = table[key]
                if mod == X % k:
                    assert (X - v) % k == 0
                    s = (X - v) // k
                    ret = min(ret, s)

    return ret


def main():
    N, X = map(int, input().split())
    AS = list(map(int, input().split()))
    print(solve(X, AS))


def solve_hahho(a, x):
    # from https://atcoder.jp/contests/abc192/submissions/20344598
    def max2(x, y): return x if x > y else y
    def min2(x, y): return x if x < y else y
    n = len(a)
    res = 2**60
    for k in range(1, n+1):
        dp = [[-2**60]*k for _ in range(k+1)]  # [chosen][reminder]
        dp[0][0] = 0
        for i_max, v in enumerate(a):
            s = v % k
            for i in reversed(range(1, min2(i_max+1, k)+1)):
                for j in range(k):
                    dp[i][j] = max2(dp[i][j], dp[i-1][(j-s) % k]+v)
        if dp[-1][x % k] >= 0:
            res = min2(res, (x-dp[-1][x % k])//k)
    return res


def random_test():
    from random import seed, randint
    N = 3
    for s in range(10000):
        seed(s)
        # X = randint(10**9, 10**18)
        # AS = [randint(1, 10**7) for i in range(N)]
        X = randint(100, 1000)
        AS = [randint(1, 10) for i in range(N)]
        me = solve(X, AS)
        op = solve_hahho(AS, X)
        if me != op:
            print(X, AS, me, op)


# random_test()

# tests
T1 = """
3 9999999999
3 6 8
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
4999999994
"""
T2 = """
1 1000000000000000000
1
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
999999999999999999
"""
T3 = """
3 12
1 2 3
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
2
"""
T4 = """
3 15
1 2 3
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
3
"""
T6 = """
3 14
1 2 3
"""
TEST_T6 = """
>>> as_input(T6)
>>> main()
5
"""
T7 = """
3 13
1 2 3
"""
TEST_T7 = """
>>> as_input(T7)
>>> main()
4
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
