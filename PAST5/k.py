# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(S):
    INF = 9223372036854775807
    table = [0] * (2 ** 16)
    for subset in range(1, 2 ** 16):
        exp = INF
        for i in range(16):  # target
            e = 0
            d = 0
            mask = 1 << i
            if subset & mask:
                e += table[subset ^ mask]
                d += 1

            y, x = divmod(i, 4)
            if x > 0:
                mask = 1 << (i - 1)
                if subset & mask:
                    e += table[subset ^ mask]
                    d += 1
            if x < 3:
                mask = 1 << (i + 1)
                if subset & mask:
                    e += table[subset ^ mask]
                    d += 1

            if y > 0:
                mask = 1 << (i - 4)
                if subset & mask:
                    e += table[subset ^ mask]
                    d += 1

            if y < 3:
                mask = 1 << (i + 4)
                if subset & mask:
                    e += table[subset ^ mask]
                    d += 1

            e += 5
            if d == 0:
                continue
            e /= d
            exp = min(exp, e)
        table[subset] = exp
    pos = 0
    for c in S:
        pos *= 2
        if c == "#":
            pos += 1
    return table[pos]


def main():
    # parse input
    S = ""
    for i in range(4):
        S += input().strip().decode('ascii')

    print(solve(S))


# tests
T1 = """
#...
....
....
....
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
5.0
"""

T2 = """
#...
#...
....
....
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
7.5
"""

T3 = """
.#..
#.#.
.#..
....
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
10.416666666666666
"""

T4 = """
###.
####
####
####
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
32.5674089515274
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
