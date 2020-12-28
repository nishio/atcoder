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

HUGE = False


def readMap(H, W, sentinel=1, encoding=_ENC1):
    global SENTINEL, HEIGHT, WIDTH
    global ORIGINAL_HEIGHT, ORIGINAL_WIDTH
    SENTINEL = sentinel
    ORIGINAL_HEIGHT = H
    ORIGINAL_WIDTH = W
    HEIGHT = H + SENTINEL * 2
    WIDTH = W + SENTINEL * 2
    data = [encoding["SENTINEL"]] * (HEIGHT * WIDTH)
    if HUGE:
        for i in range(H):
            y = (i + SENTINEL) * WIDTH
            for j in range(W):
                data[y + (j + SENTINEL)] = 1

    else:
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


def solve(H, W, R, C, world):
    visited = [False] * (WIDTH * HEIGHT)
    stack = {WIDTH * R + C}

    while len(stack) > 0:
        pos = stack.pop()
        visited[pos] = True

        next = pos - 1
        if not visited[next]:
            if world[next] == 1 or world[next] == 2:
                stack.add(next)

        next = pos + 1
        if not visited[next]:
            if world[next] == 1 or world[next] == 3:
                stack.add(next)

        next = pos + WIDTH
        if not visited[next]:
            if world[next] == 1 or world[next] == 4:
                stack.add(next)

        next = pos - WIDTH
        if not visited[next]:
            if world[next] == 1 or world[next] == 5:
                stack.add(next)

    for y in range(ORIGINAL_HEIGHT):
        line = []
        for x in range(ORIGINAL_WIDTH):
            pos = WIDTH + 1 + WIDTH * y + x
            if world[pos] == 0:
                line.append("#")
            elif visited[pos]:
                line.append("o")
            else:
                line.append("x")
        print("".join(line))


def main():
    # parse input
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    enc = {
        ord("."): 1, ord(">"): 2, ord("<"): 3,
        ord("^"): 4, ord("v"): 5, "ELSE": 0, "SENTINEL": 0}
    world = readMap(H, W, sentinel=1, encoding=enc)
    solve(H, W, R, C, world)


# tests
T1 = """
3 3
1 1
..#
^^.
><.
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
oo#
ooo
xxo
"""

T2 = """
10 12
9 1
#.^<..><<...
#<>.#<^.<<.^
^.<>.^.^.^>.
^.>#^><#....
.>.^>#...<<>
....^^.#<.<.
.>^..^#><#.^
......#>....
..<#<...^>^.
<..^>^^...^<
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
#xxxxxxxxxxx
#xxx#xxxxxxx
xooxxxxxxxxx
xox#xxx#xxxx
oooxx#xxxxxx
ooooxxx#xxxx
ooooox#xx#xx
oooooo#xxxxx
ooo#xoooxxxx
xooxooooooxx
"""

T3 = """
15 20
13 9
####..<#^>#>.<<><^..
#.>#>.^#^.>><>...^..
>..<>.#.>.>.>...#..<
<^>.#..<>^#<#.>.<.^.
>#<^>.>#^>#^.^.#^><^
<^.^.#<...<.><#>...#
.<>....^..#>>#..>>><
.<#<^#.>#>^^.>.##.^<
.#.^.....<<#^#><^<<<
^.#>.#^.>.^.^<<>..><
.^#^<^^^<......^>.#^
.<..#>...^>^.^<..<.^
#.^.#..#.....>#.^^.>
.#^..>>><>>>^..#^.^^
.>#..<..<>.#>..^.#.^
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
####xxx#xx#xxxxxxxxx
#xx#xxx#xxxxxxxxxxxx
xxxxxx#xxxxxxxxx#xxx
xxxx#xxxxx#x#xxxxxxx
x#xxxxx#xx#xxxx#xxxx
xxoxo#xxxxxxxx#xxxx#
xxoooooxxx#xx#xxxxxx
xx#xo#ox#xxxxxx##xxx
x#xxooooooo#x#xxxxxx
xx#oo#ooooooxxxoooxx
xx#ooxoooooooooooo#x
xxoo#oooooooooooooox
#ooo#oo#ooooox#oooox
x#oooxxxxoooooo#ooox
xx#oooooooo#oooxo#ox
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
    if HUGE:
        solve(1000, 1000, 1, 1, readMap(1000, 1000))
    else:
        main()
    sys.exit()

# end of snippets/main.py
