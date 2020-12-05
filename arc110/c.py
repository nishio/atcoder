# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, PS):
    ret = []
    used = [False] * (N - 1)

    def swap(x):
        PS[x - 1], PS[x] = PS[x], PS[x - 1]
        used[x - 1] = True
        ret.append(x)

    for target in range(1, N):
        x = PS.index(target, target - 1)
        for i in range(x, target - 1, -1):
            if used[i - 1]:
                return [-1]
            swap(i)
        # debug(PS, msg=":PS")

    # debug(used, msg=":used")
    if False in used:
        return [-1]
    return ret


def main():
    # parse input
    N = int(input())
    PS = list(map(int, input().split()))
    print(*solve(N, PS), sep="\n")


# tests
T1 = """
4
2 3 4 1
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
3
2
1
"""

T01 = """
5
2 4 1 5 3
"""
TEST_T01 = """
>>> as_input(T01)
>>> main()
2
1
4
3
"""

T3 = """
5
5 4 3 2 1
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
-1
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
