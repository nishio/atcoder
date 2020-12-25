# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(D, L, N, CS, KFTS):
    MAX_C = 10 ** 5
    first = [None] * MAX_C
    prev = [None] * MAX_C
    next = [None] * D
    for i, d in enumerate(CS):
        d -= 1  # to 0-origin
        if first[d] is None:
            first[d] = i
            prev[d] = i
        else:
            next[prev[d]] = i
            prev[d] = i
    for d in range(MAX_C):
        if prev[d] is not None:
            next[prev[d]] = D + first[d]

    for K, F, T in KFTS:
        F -= 1  # 1-origin to 0-origin
        ret = 0
        if CS[F % D] == K:
            ret = 1
        countdown = T - 1
        cur = F
        prev = cur
        while countdown:
            cur += 1
            if CS[cur % D] == K:
                ret += 1
                countdown -= 1
                while True:
                    n = next[cur % D]
                    d = n - cur
                    if d < 0:
                        d += D
                    up = (d - 1) // L + 1
                    if countdown >= up:
                        countdown -= up
                        cur = n
                        ret += 1
                        continue
                    else:
                        countdown = 0
                        break

            elif cur - prev == L:
                prev = cur
                countdown -= 1
        print(ret)


def main():
    # parse input
    D, L, N = map(int, input().split())
    CS = list(map(int, input().split()))
    KFTS = []
    for _i in range(N):
        KFTS.append(tuple(map(int, input().split())))
    solve(D, L, N, CS, KFTS)


# tests
T1 = """
4 2 3
2 3 1 3
1 2 2
3 3 1
3 4 3
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
1
0
3
"""

T2 = """
3 1 3
1 1 1
2 1 3
1 2 3
1 3 3
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
0
3
3
"""

T3 = """
10 4 4
4 4 4 3 1 1 5 2 2 1
2 5 2
2 9 10
2 3 3
2 7 13
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
1
5
1
6
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
