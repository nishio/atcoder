# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    MOD = 998_244_353
    H, W, K = map(int, input().split())
    CS = [0] * ((H + 2) * (W + 2))
    for _k in range(K):
        h, w, c = input().strip().split()
        CS[(int(h) * (W + 2) + int(w))] = ord(c)

    from collections import defaultdict
    table = defaultdict(int)
    table = [0] * ((H + 2) * (W + 2))
    v = table[1 + (W + 2)] = 1
    for h in range(1, H + 1):
        for w in range(1, W + 1):
            pos = h * (W + 2) + w
            # debug(pos, table[pos], msg=":pos, table[pos]")
            v = table[pos] % MOD
            # c = value.get((h, w))
            c = CS[pos]
            if c == 88:  # "X":
                table[pos + 1] += v * 3
                table[pos + (W + 2)] += v * 3
            elif c == 68:  # "D":
                table[pos + (W + 2)] += v * 3
            elif c == 82:  # "R":
                table[pos + 1] += v * 3
            else:
                table[pos + 1] += v * 2
                table[pos + (W + 2)] += v * 2

    ret = table[H * (W + 2) + W] % MOD
    LEN = (H + W - 2)
    NEGK = H * W - K

    ret *= pow(3, (MOD - 1 - (LEN - NEGK)), MOD)
    ret %= MOD
    print(ret)


# tests
T1 = """
2 2 3
1 1 X
2 1 R
2 2 R
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
5
"""

T2 = """
3 3 5
2 3 D
1 3 D
2 1 D
1 2 X
3 1 R
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
150
"""

T3 = """
5000 5000 10
585 1323 R
2633 3788 X
1222 4989 D
1456 4841 X
2115 3191 R
2120 4450 X
4325 2864 X
222 3205 D
2134 2388 X
2262 3565 R
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
result
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
