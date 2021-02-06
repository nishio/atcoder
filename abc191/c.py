# included from libs/readMap.py
"""
read map from stdin into one-dimension list with sentinel
"""
HASH, DOT, LEFT, RIGHT, UP, DOWN = b"#.<>^v"


class OneDimensionMap:
    def __init__(self, H, W, SENTINEL=0, S_CHAR=HASH):
        self.ORIGINAL_HEIGHT = H
        self.ORIGINAL_WIDTH = W
        self.rawdata = []
        for _i in range(H):
            S = input().strip()
            self.rawdata.append(S)

        self.SENTINEL = SENTINEL
        self.HEIGHT = HEIGHT = self.ORIGINAL_HEIGHT + SENTINEL * 2
        self.WIDTH = WIDTH = self.ORIGINAL_WIDTH + SENTINEL * 2
        data = [S_CHAR] * (HEIGHT * WIDTH)

        for i in range(self.ORIGINAL_HEIGHT):
            S = self.rawdata[i]
            y = (i + SENTINEL) * WIDTH
            for j in range(self.ORIGINAL_WIDTH):
                data[y + (j + SENTINEL)] = S[j]
        self.mapdata = data

    def allPosition(self):
        S = self.SENTINEL
        for y in range(self.ORIGINAL_HEIGHT):
            for x in range(self.ORIGINAL_WIDTH):
                yield self.WIDTH * (y + S) + (x + S)

    def dfs(self, start):
        # sample from PAST5H
        visited = [False] * (self.WIDTH * self.HEIGHT)
        stack = {start}
        mapdata = self.mapdata

        while len(stack) > 0:
            pos = stack.pop()
            visited[pos] = True

            next = pos - 1
            if not visited[next]:
                if mapdata[next] == DOT or mapdata[next] == RIGHT:
                    stack.add(next)

            next = pos + 1
            if not visited[next]:
                if mapdata[next] == DOT or mapdata[next] == LEFT:
                    stack.add(next)

            next = pos + self.WIDTH
            if not visited[next]:
                if mapdata[next] == DOT or mapdata[next] == UP:
                    stack.add(next)

            next = pos - self.WIDTH
            if not visited[next]:
                if mapdata[next] == DOT or mapdata[next] == DOWN:
                    stack.add(next)
        return visited

    def print2d(self, values=None):
        # sample from PAST5H
        S = self.SENTINEL
        for y in range(self.ORIGINAL_HEIGHT):
            line = []
            for x in range(self.ORIGINAL_WIDTH):
                pos = self.WIDTH * (y + S) + (x + S)
                if self.mapdata[pos] == HASH:
                    line.append("#")
                elif values is None:
                    line.append(chr(self.mapdata[pos]))
                elif values[pos]:
                    line.append("o")
                else:
                    line.append("x")
            print("".join(line))

    def dir9(self):
        W = self.WIDTH
        return [
            -1 - W, -W, 1 - W,
            -1, 0, 1,
            W - 1, W, W + 1
        ]

    def dir8(self):
        W = self.WIDTH
        return [
            -1 - W, -W, 1 - W,
            -1, 1,
            W - 1, W, W + 1
        ]

    def dir4(self):
        W = self.WIDTH
        return [-W, -1, 1, W]

    def rotate(self):
        # from PAST5E
        W, H = self.WIDTH, self.HEIGHT
        newdata = [0] * (W * H)
        for x in range(H):
            for y in range(W):
                newdata[y * H + x] = self.mapdata[(H - 1 - x) * W + y]
        self.mapdata = newdata
        self.WIDTH, self.HEIGHT = H, W

# end of libs/readMap.py
# included from snippets/main.py


def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    H, W = map(int, input().split())
    world = OneDimensionMap(H, W, 0)
    from collections import defaultdict
    cornerCount = defaultdict(int)
    for pos in world.allPosition():
        if world.mapdata[pos] == 35:
            for d in [0, 1, W, 1 + W]:
                cornerCount[pos + d] += 1

    print(sum(v % 2 for v in cornerCount.values()))


# tests
T1 = """
5 5
.....
.###.
.###.
.###.
.....
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
4
"""

T2 = """
5 6
......
.###..
.#....
.###..
......
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
8
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
