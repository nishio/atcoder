# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, CS):
    MOD = 1_000_000_007
    prev = CS[0]
    count = 1
    for i in range(1, N):
        x = CS[i]
        if x != prev:
            count += 1
            prev = x

    if count == 2:
        return 1
    ret = -1
    ret += pow(2, (count - 2) // 2, MOD)
    ret += pow(2, (count - 1) // 2, MOD)
    return ret % MOD


def main():
    # parse input
    N = int(input())
    CS = []
    for _i in range(N):
        CS.append(int(input()))
    print(solve(N, CS))


# tests
T1 = """
5
1
2
1
2
2
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
3
"""

T2 = """
6
4
2
5
4
2
4
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
5
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
