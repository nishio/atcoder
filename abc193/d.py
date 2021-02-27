# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    K = int(input())
    S = input().strip().decode('ascii')
    T = input().strip().decode('ascii')
    scount = [0] * 9
    tcount = [0] * 9
    rest = [K] * 9
    for i in range(4):
        s = int(S[i]) - 1
        t = int(T[i]) - 1
        scount[s] += 1
        tcount[t] += 1
        rest[s] -= 1
        rest[t] -= 1

    def calcScore(xs):
        ret = 0
        for i in range(9):
            ret += (i + 1) * (10 ** xs[i])
        return ret

    ret = 0
    for a in range(9):
        if rest[a] == 0:
            continue
        pa = rest[a]
        rest[a] -= 1
        scount[a] += 1

        for b in range(9):
            if rest[b] == 0:
                continue
            pb = rest[b]
            tcount[b] += 1
            if calcScore(scount) > calcScore(tcount):
                ret += pa * pb
            tcount[b] -= 1

        rest[a] += 1
        scount[a] -= 1

    ret /= (9 * K - 8) * (9 * K - 9)
    print(ret)


# tests
T1 = """
2
1144#
2233#
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
0.4444444444444444
"""
T2 = """
2
9988#
1122#
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
1.0
"""
T3 = """
6
1122#
2228#
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
0.001932367149758454
"""
T4 = """
100000
3226#
3597#
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
0.6296297942426154
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
