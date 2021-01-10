# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    N, C = map(int, input().split())
    from collections import defaultdict
    diff = defaultdict(int)
    for _n in range(N):
        a, b, c = map(int, input().split())
        diff[a] += c
        diff[b + 1] -= c
    keys = list(sorted(diff))
    cost = 0
    ret = 0
    for i in range(1, len(keys)):
        cost += diff[keys[i - 1]]
        days = keys[i] - keys[i - 1]
        ret += min(cost, C) * days

    print(ret)


# tests
T1 = """
2 6
1 2 4
2 2 4
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
10
"""

T2 = """
5 1000000000
583563238 820642330 44577
136809000 653199778 90962
54601291 785892285 50554
5797762 453599267 65697
468677897 916692569 87409
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
163089627821228
"""
T3 = """
5 100000
583563238 820642330 44577
136809000 653199778 90962
54601291 785892285 50554
5797762 453599267 65697
468677897 916692569 87409

"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
88206004785464
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
