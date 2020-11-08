# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, X, AS):
    digits = []
    mods = []
    x = X
    for i in range(1, N):
        m = AS[i] // AS[i - 1]
        mods.insert(0, m)
        q, r = divmod(x, m)
        digits.insert(0, r)
        x = q
    digits.insert(0, x)
    mods.insert(0, 0)

    ret = 1
    for i in range(N):
        if digits[i] + 1 != mods[i]:
            # can increment
            # debug(i, digits[i], mods[i], msg=":i, digits[i], mods[i]")
            for j in range(i + 1, N):
                if digits[j] != 0:
                    ret += 1
    # debug(digits, msg=":digits")
    # debug(mods, msg=":mods")
    return ret


def ac(n, x, A):
    # https://atcoder.jp/contests/abc182/submissions/17989253
    lowcnt = 1

    highcnt = 1

    low = x
    high = x
    for a in A[1:]:
        if high == low:
            if high % a:
                low = high // a * a
                high = low + a
        else:
            nxtlow = lowcnt
            nxthigh = highcnt
            if high % a:
                nxtlow += highcnt
            if low % a:
                nxthigh += lowcnt
            lowcnt = nxtlow
            highcnt = nxthigh
            low = low // a * a
            high = low + a

    return (highcnt + lowcnt if high - low else highcnt)


def main():
    # parse input
    N, X = map(int, input().split())
    AS = list(map(int, input().split()))
    print(solve(N, X, AS))


# tests
T1 = """
3 9
1 5 10
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
3
"""

T2 = """
5 198
1 5 10 50 100
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
5
"""

T3 = """
4 44
1 4 20 100
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
4
"""

T4 = """
9 11837029798
1 942454037 2827362111 19791534777 257289952101 771869856303 3859349281515 30874794252120 216123559764840
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
21
"""

T5 = """
4 1
1 10 100 1000
"""
TEST_T5 = """
>>> as_input(T5)
>>> main()
4
"""

T6 = """
4 11
1 10 100 1000
"""
TEST_T6 = """
>>> as_input(T6)
>>> main()
6
"""

T7 = """
4 10
1 10 100 1000
"""
TEST_T7 = """
>>> as_input(T7)
>>> main()
3
"""

T8 = """
4 99
1 10 100 1000
"""
TEST_T8 = """
>>> as_input(T8)
>>> main()
5
"""

T9 = """
5 101
1 10 100 1000 10000
"""
TEST_T9 = """
>>> as_input(T9)
>>> main()
7
"""


def random_test():
    from random import randint
    AS = [1, 2, 4, 8]
    N = len(AS)
    for i in range(2000):
        r1 = solve(N, i, AS)
        r2 = ac(N, i, AS)
        if r1 != r2:
            print(i, r1, r2)


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
        random_test()
        sys.exit()
    main()
    sys.exit()

# end of snippets/main.py
