# included from libs/readMap.py
"""
read map from stdin into one-dimension list with sentinel
"""


def dir9():
    return [
        -1 - WIDTH, -WIDTH, 1 - WIDTH,
        -1, 0, 1,
        WIDTH - 1, WIDTH, WIDTH + 1
    ]


def dir8():
    return [
        -1 - WIDTH, -WIDTH, 1 - WIDTH,
        -1, 1,
        WIDTH - 1, WIDTH, WIDTH + 1
    ]


def dir4():
    return [-WIDTH, -1, 1, WIDTH]


_ENC1 = {ord("."): 1, "ELSE": 0, "SENTINEL": 0}


def readMap(H, W, sentinel=1, encoding=_ENC1):
    global SENTINEL, HEIGHT, WIDTH
    global ORIGINAL_HEIGHT, ORIGINAL_WIDTH
    SENTINEL = sentinel
    ORIGINAL_HEIGHT = H
    ORIGINAL_WIDTH = W
    HEIGHT = H + SENTINEL * 2
    WIDTH = W + SENTINEL * 2
    data = [encoding["SENTINEL"]] * (HEIGHT * WIDTH)
    for i in range(H):
        S = input().strip()
        y = (i + SENTINEL) * WIDTH
        for j in range(W):
            data[y + (j + SENTINEL)] = encoding.get(S[j], encoding["ELSE"])
    return data


def allPosition():
    for y in range(ORIGINAL_HEIGHT):
        for x in range(ORIGINAL_WIDTH):
            yield WIDTH + 1 + WIDTH * y + x

# end of libs/readMap.py

# included from snippets/main.py


def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(H, W, world, stamp):
    S = max(H, W)
    # world
    WW = W + 2 * S
    WH = H + 2 * S
    # stamp
    SW = W
    SH = H

    def conflict():
        for x in range(SW):
            for y in range(SH):
                if stamp[y * SW + x] == 0:
                    if world[(sy + y) * WW + (sx + x)] == 0:
                        # conflict
                        return True

    for _rot in range(4):
        for sx in range(S + W):
            for sy in range(S + H):
                if conflict():
                    continue
                return True
        # rotate
        new_stamp = [0] * (W * H)
        for x in range(SH):
            for y in range(SW):
                new_stamp[y * SH + x] = stamp[(SH - 1 - x) * SW + y]
        stamp = new_stamp
        SW, SH = SH, SW

    return False


def main():
    # parse input
    H, W = map(int, input().split())
    world = readMap(H, W, max(H, W))
    stamp = readMap(H, W, 0)
    if solve(H, W, world, stamp):
        print("Yes")
    else:
        print("No")


# tests
T0 = """
2 5
..#..
.....
..##.
.###.
"""
TEST_T0 = """
>>> as_input(T0)
>>> main()
Yes
"""

T1 = """
3 3
...
.#.
..#
#.#
###
...
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
Yes
"""

T2 = """
3 3
...
#..
#.#
.#.
.##
##.
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
No
"""

T3 = """
2 5
.....
..#..
..##.
.###.
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
Yes
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