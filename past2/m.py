# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(D, L, N, CS, KFTS):
    import bisect
    MAX_C = 10 ** 5
    first = [None] * MAX_C
    prev = [None] * MAX_C
    next = [None] * D
    occur = [[] for _i in range(MAX_C)]
    for i, d in enumerate(CS):
        d -= 1  # to 0-origin
        occur[d].append(i)
        if first[d] is None:
            first[d] = i
            prev[d] = i
        else:
            next[prev[d]] = i
            prev[d] = i
    for d in range(MAX_C):
        if prev[d] is not None:
            next[prev[d]] = D + first[d]
            occur[d].append(D + first[d])

    ups = [0] * D
    for i in range(D):
        n = next[i]
        d = n - i
        if d < 0:
            d += D
        up = (d - 1) // L + 1
        ups[i] = up

    # doubling
    db_next = [next]
    db_ups = [ups]
    for _i in range(1, 30):
        next = db_next[-1]
        ups = db_ups[-1]
        new_next = []
        new_ups = []
        for i in range(D):
            n1 = next[i] % D
            n2 = next[n1]
            u1 = ups[i]
            u2 = ups[n1]
            new_next.append(n2)
            new_ups.append(u1 + u2)
        db_next.append(new_next)
        db_ups.append(new_ups)

    for K, F, T in KFTS:
        F -= 1  # 1-origin to 0-origin
        if first[K - 1] is None:
            print(0)
            continue
        ret = 0
        countdown = T - 1
        cur = F
        prev = cur

        # find first occurence
        i = bisect.bisect_left(occur[K - 1], F)
        oc = occur[K - 1][i]
        up = (oc - cur - 1) // L + 1
        if up > countdown:
            print(0)
            continue
        countdown -= up
        ret += 1
        cur = oc % D
        # doubling binary search
        for i in range(30 - 1, -1, -1):
            up = db_ups[i][cur % D]
            if countdown >= up:
                countdown -= up
                cur = db_next[i][cur % D]
                ret += 2 ** i

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
