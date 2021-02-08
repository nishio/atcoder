# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass

# included from libs/binary_search.py


def binary_search_int(f, left=0, right=1000000):
    while left < right - 1:
        x = (left + right) // 2
        y = f(x)
        if y < 0:
            left = x
        else:
            right = x
    return right


def binary_search_float(f, left=0.0, right=1000000.0, eps=10**-7):
    while left < right - eps:
        x = (left + right) / 2
        y = f(x)
        if y < 0:
            left = x
        else:
            right = x
    return right

# end of libs/binary_search.py


def main():
    from math import floor, ceil, sqrt
    fX, fY, fR = map(float, input().split())
    X, Y, R = [round(x * 10000) for x in [fX, fY, fR]]
    ret = 0

    def isIn(x, y):
        ret = (X - x * 10000) ** 2 + (Y - y * 10000) ** 2 <= R ** 2
        return ret

    for y in range(floor(fY - fR), ceil(fY + fR) + 1):
        # find start
        left = floor(fX - fR - 1)
        init_right = right = floor(fX)
        if isIn(right, y):
            while left < right - 1:
                x = (left + right) // 2
                if isIn(x, y):
                    right = x
                else:
                    left = x
            ret += init_right - left

        # find end
        init_left = left = init_right + 1
        right = ceil(fX + fR + 1)
        if isIn(left, y):
            while left < right - 1:
                x = (left + right) // 2
                if isIn(x, y):
                    left = x
                else:
                    right = x
            ret += right - init_left

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
