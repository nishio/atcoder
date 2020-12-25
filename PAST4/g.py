# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


# included from libs/readMap.py
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
    data = [101] * (HEIGHT * WIDTH)
    ok = ord(".")
    for i in range(H):
        S = input().strip()
        y = (i + SENTINEL) * WIDTH
        for j in range(W):
            data[y + (j + SENTINEL)] = 100 if S[j] == ok else 101
    return data


def allPosition():
    for y in range(ORIGINAL_HEIGHT):
        for x in range(ORIGINAL_WIDTH):
            yield WIDTH + 1 + WIDTH * y + x


# end of libs/readMap.py

def solve(H, W, data):
    DOT = 100
    BLOCK = 101

    def paint(pos, color):
        data[pos] = color
        for d in [-WIDTH, -1, +1, +WIDTH]:
            if data[pos + d] == DOT:
                paint(pos + d, color)

    # debug(data, msg=":data")
    color = 0
    for pos in allPosition():
        if data[pos] == DOT:
            paint(pos, color)
            color += 1

    # debug(data, msg=":data")
    # debug(color, msg=":color")
    if color >= 5:
        return 0
    ret = 0
    for pos in allPosition():
        if data[pos] != BLOCK:
            continue
        color_exists = [0] * 4
        for d in [-WIDTH, -1, +1, +WIDTH]:
            c = data[pos + d]
            if c < 4:
                color_exists[c] = 1
        if sum(color_exists) == color:
            ret += 1

    return ret


def main():
    # parse input
    H, W = map(int, input().split())
    data = readMap(H, W)
    print(solve(H, W, data))


# tests
T1 = """
3 3
..#
#..
.##
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
2
"""

T2 = """
3 3
##.
##.
...
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
3
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
