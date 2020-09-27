"""
Floor sum
"""


def floor_sum(n, m, a, b):
    ret = 0
    while True:
        if a >= m:
            ret += (a // m) * (n - 1) * n // 2
            a %= m
        if b >= m:
            ret += n * (b // m)
            b %= m
        if a * n + b < m:
            return ret
        y_max = (a * n + b) // m
        x_max = y_max * m - b
        ret += (n - (x_max + a - 1) // a) * y_max
        n, m, a, b = y_max, a, m, -x_max % a

# --- end of library ---


def main():
    # verified: https://atcoder.jp/contests/practice2/tasks/practice2_c
    T = int(input())
    for _t in range(T):
        N, M, A, B = map(int, input().split())
        print(floor_sum(N, M, A, B))


def _test():
    import doctest
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
            doctest.run_docstring_examples(g[k], g, name=k)


T1 = """
5
4 10 6 3
6 5 4 3
1 1 0 0
31415 92653 58979 32384
1000000000 1000000000 999999999 999999999
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
3
13
0
314095480
499999999500000000
"""


def as_input(s):
    "use in test, use given string as input file"
    import io
    g = globals()
    f = io.StringIO(s.strip())

    g["input"] = lambda: bytes(f.readline(), "ascii")
    g["read"] = lambda: bytes(f.read(), "ascii")


if __name__ == "__main__":
    import sys
    input = sys.stdin.buffer.readline
    if sys.argv[-1] == "-t":
        print("testing")
        _test()
        sys.exit()
    main()
