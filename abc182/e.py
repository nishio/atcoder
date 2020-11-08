# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(H, W, mapdata):
    maph = mapdata[:]
    for y in range(H):
        ypos = y * W
        for x in range(1, W):
            pos = ypos + x
            if maph[pos] == 0 and maph[pos - 1] == 1:
                maph[pos] = 1

        for x in range(W - 2, -1, -1):
            pos = ypos + x
            if maph[pos] == 0 and maph[pos + 1] == 1:
                maph[pos] = 1

    mapv = mapdata[:]
    for x in range(W):
        for y in range(1, H):
            pos = y * W + x
            if mapv[pos] == 0 and mapv[pos - W] == 1:
                mapv[pos] = 1

        for y in range(H - 2, -1, -1):
            pos = y * W + x
            if mapv[pos] == 0 and mapv[pos + W] == 1:
                mapv[pos] = 1

    ret = 0
    for i in range(W * H):
        if maph[i] == 1 or mapv[i] == 1:
            ret += 1
    return ret


def main():
    H, W, N, M = map(int, input().split())
    mapdata = [0] * (H * W + 10)
    for _i in range(N):
        A, B = map(int, input().split())
        mapdata[(A - 1) * W + B - 1] = 1

    for _i in range(M):
        A, B = map(int, input().split())
        mapdata[(A - 1) * W + B - 1] = -1

    # parse input
    print(solve(H, W, mapdata))


# tests
T1 = """
3 3 2 1
1 1
2 3
2 2
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
7
"""

T2 = """
4 4 3 3
1 2
1 3
3 4
2 3
2 4
3 2
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
8
"""

T3 = """
5 5 5 1
1 1
2 2
3 3
4 4
5 5
4 2
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
24
"""

T4 = """
5 5 1 0
3 3
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
9
"""

T5 = """
1 5 1 0
3 1
"""
TEST_T5 = """
>>> as_input(T5)
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
