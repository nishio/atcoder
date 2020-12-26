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
    from collections import defaultdict
    # make graph
    edges = defaultdict(list)
    count = 0
    a_vertex = None
    for x in range(H):
        for y in range(W):
            v = W * x + y
            pos = WIDTH + 1 + WIDTH * x + y
            if data[pos]:
                a_vertex = v
                count += 1
                if data[pos + 1]:
                    edges[v].append(v + 1)
                    edges[v + 1].append(v)
                if data[pos + WIDTH]:
                    edges[v].append(v + W)
                    edges[v + W].append(v)

    if count == 1:
        print(1)
        v = a_vertex
        x, y = divmod(v, W)
        print(x + 1, y + 1)

    for start in edges:
        visited = [False] * (H * W)
        path = []

        def visit(cur):
            visited[cur] = True
            path.append(cur)
            if len(path) == count:
                return True
            for next in edges[cur]:
                if not visited[next]:
                    r = visit(next)
                    if r:
                        return True
            visited[cur] = False
            path.pop()

        if visit(start):
            print(count)
            for v in path:
                x, y = divmod(v, W)
                print(x + 1, y + 1)
            return


def main():
    # parse input
    H, W = map(int, input().split())
    data = readMap(H, W, 1, {ord("#"): 1, "ELSE": 0, "SENTINEL": 0})
    solve(H, W, data)


# tests
T1 = """
3 3
##.
.##
###
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
7
1 1
1 2
2 2
2 3
3 3
3 2
3 1
"""

T2 = """
3 4
####
####
.#..
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
9
2 1
1 1
1 2
1 3
1 4
2 4
2 3
2 2
3 2
"""

T4 = """
3 3
.##
###
###
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
8
1 2
1 3
2 3
2 2
2 1
3 1
3 2
3 3
"""

T5 = """
1 1
#
"""
TEST_T5 = """
>>> as_input(T5)
>>> main()
1
1 1
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
