# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    N = int(input())
    CS = []
    sums = []
    for _i in range(N):
        row = tuple(map(int, input().split()))
        CS.append(row) 
        sums.append(sum(row))

    m = min(sums)
    if any((x - m) % N for x in sums):
        print("No")
        return

    AS = [(x - m) // N for x in sums]
    BS = [x - AS[0] for x in CS[0]]
    print("Yes")
    print(*AS)
    print(*BS)

# tests
T1 = """
3
4 3 5
2 1 3
3 2 4
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
Yes
2 0 1
2 1 3
"""
T2 = """
3
4 3 5
2 2 3
3 2 4
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
No
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