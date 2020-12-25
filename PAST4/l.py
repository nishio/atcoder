# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    import sys
    sys.setrecursionlimit(10 ** 6)
    INF = sys.maxsize  # float("inf")
    MOD = 10 ** 9 + 7  # 998_244_353


def main():
    # parse input
    N, Q = map(int, input().split())
    HS = list(map(int, input().split()))
    from collections import defaultdict
    freq = defaultdict(int)
    for i in range(N - 1):
        d = HS[i] - HS[i + 1]  # odd - even
        if i & 1:
            d = -d
        freq[d] += 1

    odd_height = 0
    for _q in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            odd_height += q[1]
            print(freq[-odd_height])
        elif q[0] == 2:
            odd_height -= q[1]
            print(freq[-odd_height])
        else:
            i = q[1] - 1
            add = q[2]
            if i > 0:
                d = HS[i] - HS[i - 1]
                if i & 1:
                    d = -d
                freq[d] -= 1
            if i < N - 1:
                d = HS[i] - HS[i + 1]
                if i & 1:
                    d = -d
                freq[d] -= 1

            HS[i] += add
            if i > 0:
                d = HS[i] - HS[i - 1]
                if i & 1:
                    d = -d
                freq[d] += 1
            if i < N - 1:
                d = HS[i] - HS[i + 1]
                if i & 1:
                    d = -d
                freq[d] += 1
            print(freq[-odd_height])


# tests
T1 = """
4 2
10 20 30 20
1 10
3 4 20
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
1
2
"""

T2 = """
10 20
108 112 112 110 110 109 108 110 111 112
3 4 2
1 1
3 9 1
3 4 2
2 1
1 1
3 7 2
2 1
3 8 2
1 1
2 1
1 1
3 10 2
3 6 1
2 1
3 7 1
1 1
2 1
3 3 2
3 3 2
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
2
2
1
1
2
1
0
3
3
0
3
0
0
0
4
3
1
3
3
2
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
