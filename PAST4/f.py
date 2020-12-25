# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, K, SS):
    from collections import Counter
    c = Counter(SS).most_common()
    K -= 1
    ck, ckv = c[K]
    if K > 0:
        _, pv = c[K - 1]
        if pv == ckv:
            return "AMBIGUOUS"
    if K < len(c) - 1:
        _, pv = c[K + 1]
        if pv == ckv:
            return "AMBIGUOUS"
    return ck


def main():
    # parse input
    N, K = map(int, input().split())
    SS = read().strip().decode('ascii').split("\n")
    print(solve(N, K, SS))


# tests
T1 = """
6 2
abcde
caac
abcde
caac
abc
caac
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
abcde
"""

T2 = """
9 3
a
a
bb
bb
a
ccc
bb
ccc
dddd
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
ccc
"""

T3 = """
7 2
caac
abcde
caac
abc
abcde
caac
abc
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
AMBIGUOUS
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
