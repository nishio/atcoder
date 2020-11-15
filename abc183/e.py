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


def solve(H, W, data):
    MOD = 1_000_000_007
    N = len(data)
    h_accum = [0] * N
    v_accum = [0] * N
    d_accum = [0] * N
    table = [0] * N
    table[WIDTH + 1] = 1
    for pos in allPosition():
        if pos == WIDTH + 1:
            continue
        hvalue = 0
        p = pos
        while True:
            p -= 1
            if data[p] == 0:
                break
            hvalue += table[p]

        vvalue = 0
        p = pos
        while True:
            p -= WIDTH
            if data[p] == 0:
                break
            vvalue += table[p]

        dvalue = 0
        p = pos
        while True:
            p -= (WIDTH + 1)
            if data[p] == 0:
                break
            dvalue += table[p]

        ret = hvalue + vvalue + dvalue
        ret %= MOD
        table[pos] = ret

    return ret


def main():
    # parse input
    H, W = map(int, input().split())
    data = readMap(H, W, sentinel=1, encoding=_ENC1)
    print(solve(H, W, data))


# tests
T1 = """
3 3
...
.#.
...
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
10
"""

T2 = """
4 4
...#
....
..#.
....
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
84
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
