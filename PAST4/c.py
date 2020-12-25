# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    import sys
    sys.setrecursionlimit(10 ** 6)
    INF = sys.maxsize  # float("inf")
    MOD = 10 ** 9 + 7  # 998_244_353


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
    data = [0] * (HEIGHT * WIDTH)
    ok = ord("#")
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


# end of libs/readMap.py
def main():
    # parse input
    H, W = map(int, input().split())
    data = readMap(H, W)
    ret = []
    ds = [-1 - WIDTH, -WIDTH, 1 - WIDTH, -1,
          0, 1, WIDTH - 1, WIDTH, WIDTH + 1]
    for pos in allPosition():
        s = 0
        for d in ds:
            s += data[pos + d]
        ret.append(s)

    for y in range(H):
        print("".join(str(x) for x in ret[y * W: y * W + W]))


# tests
T1 = """
3 4
#.##
..#.
#...
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
1333
2433
1211
"""

T2 = """
10 12
#.##..#...##
#..#..##...#
##.#....##.#
.#..###...#.
#..#..#...##
###...#..###
.###.#######
.#..#....###
.#.##..####.
.###....#..#
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
233322331133
455432343354
444344443343
444344332454
454335431465
466434554686
466434445796
346554457885
346542135664
235431134432
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
