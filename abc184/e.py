# included from libs/readMap.py
"""
read map from stdin into one-dimension list with sentinel
"""


from collections import defaultdict


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

WARP = defaultdict(list)


def readMap(H, W, sentinel=1, encoding=_ENC1):
    global SENTINEL, HEIGHT, WIDTH
    global ORIGINAL_HEIGHT, ORIGINAL_WIDTH
    global START, GOAL
    from string import ascii_lowercase
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
            if S[j] == ord("S"):
                START = y + (j + SENTINEL)
            if S[j] == ord("G"):
                GOAL = y + (j + SENTINEL)
            if chr(S[j]) in ascii_lowercase:
                k = S[j] - ord("a") + 1
                WARP[k].append(y + (j + SENTINEL))
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


def solve(data):
    to_visit = [START]
    DIR4 = dir4()
    # debug(WARP, msg=":WARP")
    ret = 0
    while to_visit:
        new_visit = []
        for p in to_visit:
            if p == GOAL:
                return ret

            v = data[p]
            data[p] = -1
            # debug(p, v, msg=":p, v")
            if v > 0:  # WARP
                # debug(v, msg="warp:v")
                for p2 in WARP[v]:
                    if data[p2] >= 0:
                        data[p2] = -1
                        new_visit.append(p2)
                WARP[v] = []
            for d in DIR4:
                p2 = p + d
                if data[p2] >= 0:
                    new_visit.append(p2)
        to_visit = new_visit
        ret += 1
        # debug([divmod(x, WIDTH) for x in new_visit], msg=":new")
    return -1


def main():
    # parse input
    from string import ascii_lowercase
    H, W = map(int, input().split())
    encoding = {
        ord("."): 0, ord("#"): -1, "SENTINEL": -1, "ELSE": 0
    }
    for c in ascii_lowercase:
        encoding[ord(c)] = ord(c) - ord("a") + 1

    data = readMap(H, W, encoding=encoding)
    # debug(data, msg=":data")
    print(solve(data))


# tests
T1 = """
2 5
S.b.b
a.a.G
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
4
"""

T2 = """
11 11
S##...#c...
...#d.#.#..
..........#
.#....#...#
#.....bc...
#.##......#
.......c..#
..#........
a..........
d..#...a...
.#........G
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
14
"""

T3 = """
11 11
.#.#.e#a...
.b..##..#..
#....#.#..#
.#dd..#..#.
....#...#e.
c#.#a....#.
.....#..#.e
.#....#b.#.
.#...#..#..
......#c#G.
#..S...#...
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
-1
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
