"""
read map from stdin into one-dimension list with sentinel
"""


def readMap(H, W, sentinel=1):
    global SENTINEL, HEIGHT, WIDTH
    global ORIGINAL_HEIGHT, ORIGINAL_WIDTH
    SENTINEL = sentinel
    ORIGINAL_HEIGHT = H
    ORIGINAL_WIDTH = W
    HEIGHT = H + SENTINEL * 2
    WIDTH = W + SENTINEL * 2
    data = [0] * (HEIGHT * WIDTH)
    ok = ord(".")
    for i in range(H):
        S = input().strip()
        y = (i + SENTINEL) * WIDTH
        for j in range(W):
            data[y + (j + SENTINEL)] = 1 if S[j] == ok else 0
    return data


def allPosition():
    for y in range(ORIGINAL_HEIGHT):
        for x in range(ORIGINAL_WIDTH):
            yield WIDTH + 1 + WIDTH * y + x

# --- end of library ---


def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(data, H, W):
    ret = 0
    for i in allPosition():
        if data[i] and data[i + 1]:
            ret += 1
        if data[i] and data[i + WIDTH]:
            ret += 1
    return ret


def main():
    # verified HHKB2020B https://atcoder.jp/contests/hhkb2020/tasks/hhkb2020_b
    H, W = map(int, input().split())
    data = readMap(H, W)
    print(solve(data, H, W))


# tests
T1 = """
2 3
..#
#..
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
3
"""

T2 = """
2 2
.#
#.
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
0
"""

T3 = """
2 3
...
...
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
7
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
