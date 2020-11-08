# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, S):
    from itertools import permutations
    rS = "".join(reversed(S))
    for p in permutations(S):
        ret = "".join(p)
        if ret != S and ret != rS:
            return ret
    return "None"


def main():
    # parse input
    N = int(input())
    S = input().strip().decode('ascii')
    print(solve(N, S))


# tests
T1 = """
3
cba
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
cab
"""

T2 = """
2
aa
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
None
"""


def _test():
    import doctest
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
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
    if sys.argv[-1] == "-t":
        print("testing")
        _test()
        sys.exit()
    main()

# end of snippets/main.py
