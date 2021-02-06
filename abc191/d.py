# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    from math import floor, ceil, sqrt
    map(int, input().split())
    S = input().strip().decode('ascii')
    X, Y, R = S.split()
    X = round(float(X) * 10000)
    iX = int(X * 10000)
    Y = float(Y)
    iY = int(Y * 10000)
    R = float(R)
    iR = int(R * 10000)
    iR2 = iR * iR

    ret = 0

    def isIn(x, y):
        ret = (X - x) ** 2 + (Y - y) ** 2 <= R ** 2
        # debug(x, y, X-x, Y-y, ret, msg=":x, y, ret")
        return ret

    for y in range(floor(Y - R) - 1, ceil(Y + R) + 1 + 1):
        xcep = iR2 - (y * 10000 - iY) ** 2
        a = 100000000
        b = -20000 * iX
        c = iX ** 2 - xcep
        e = b * b - 4 * a * c
        if e < 0:
            continue
        s = sqrt(e)
        # debug(a, b, c, e, msg=":a,b,c,e")
        r1 = (-b + s) / (2 * a)
        r2 = (-b - s) / (2 * a)
        # debug(r1, r2, msg=":r1, r2")
        ret += floor(r1) - ceil(r2) + 1
        # if isIn(floor(r1) + 2, y):
        #     ret += 1
        if isIn(floor(r1) + 1, y):
            ret += 1
        if not isIn(floor(r1), y):
            ret -= 1
        # if not isIn(floor(r1) + 1, y):
        #     ret -= 1
        # if isIn(ceil(r2) - 2, y):
        #     ret += 1
        if isIn(ceil(r2) - 1, y):
            ret += 1
        if not isIn(ceil(r2), y):
            ret -= 1
        # if not isIn(ceil(r2) + 1, y):
        #     ret -= 1

    # for y in range(floor(Y - R), ceil(Y + R) + 1):
    #     xcep = R ** 2 - (y - Y) ** 2
    #     a = 1
    #     b = 2 * X
    #     # c = iX ** 2 - xcep
    #     c = X ** 2 - xcep
    #     # debug(a, b, c, msg=":a, b, c")
    #     e = b * b - 4 * a * c
    #     if e < 0:
    #         continue
    #     s = sqrt(e)
    #     r1 = (-b + s) / (2 * a)
    #     r2 = (-b - s) / (2 * a)
    #     # debug(r1, r2, msg=":r1, r2")
    #     ret += floor(r1) - ceil(r2) + 1

    print(ret)


def main_simple():
    from math import floor, ceil, sqrt
    X, Y, R = map(float, input().split())

    ret = 0
    for y in range(floor(Y - R), ceil(Y + R) + 1):
        xcep = R ** 2 - (y - Y) ** 2
        a = 1
        b = -2 * X
        c = X ** 2 - xcep
        e = b * b - 4 * a * c
        if e < 0:
            continue
        s = sqrt(e)
        r1 = (-b + s) / (2 * a)
        r2 = (-b - s) / (2 * a)
        ret += floor(r1) - ceil(r2) + 1

    print(ret)


# tests
T1 = """
0.2 0.8 1.1
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
3
"""

T2 = """
100 100 1
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
5
"""

T22 = """
0 0 1
"""
TEST_T22 = """
>>> as_input(T22)
>>> main()
5
"""
T3 = """
42782.4720 31949.0192 99999.99
"""
_TEST_T3 = """
>>> as_input(T3)
>>> main()
31415920098
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
