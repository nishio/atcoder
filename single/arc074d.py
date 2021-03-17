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

    def allEdges(self):
        assert self.ORIGINAL_HEIGHT > 1 and self.ORIGINAL_WIDTH > 1
        S = self.SENTINEL
        W = self.WIDTH
        for y in range(self.ORIGINAL_HEIGHT):
            for x in range(self.ORIGINAL_WIDTH - 1):
                pos = W * (y + S) + (x + S)
                yield (pos, pos + 1)

        for y in range(self.ORIGINAL_HEIGHT - 1):
            for x in range(self.ORIGINAL_WIDTH):
                pos = W * (y + S) + (x + S)
                yield (pos, pos + W)

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
# included from libs/dinic_maxflow.py
"""
Dinic: MaxFlow
"""

from collections import defaultdict
from collections import deque


class Dinic:
    def __init__(self, numVertex):
        from collections import defaultdict
        self.numVertex = numVertex
        self.edges = defaultdict(lambda: defaultdict(int))

    def add_edge(self, frm, to, capacity, bidirectional=False):
        if bidirectional:
            self.edges[frm][to] = capacity
            self.edges[to][frm] = capacity
        else:
            self.edges[frm][to] = capacity
            self.edges[to][frm] += 0  # assure to exists

    def debug_edges(self):
        ret = "\n"
        def to_s(d):
            return ", ".join(f"{k}: {d[k]}" for k in d)
        
        for frm in self.edges:
            ret += f"{frm}:\n\t{to_s(self.edges[frm])}\n"
        return ret

    def bfs(self, start, goal):
        """
        update: distance_from_start
        return bool: can reach to goal
        """
        self.distance_from_start = [-1] * self.numVertex
        queue = deque()
        self.distance_from_start[start] = 0
        queue.append(start)
        while queue and self.distance_from_start[goal] == -1:
            frm = queue.popleft()
            for to in self.edges[frm]:
                if self.edges[frm][to] > 0 and self.distance_from_start[to] == -1:
                    self.distance_from_start[to] = self.distance_from_start[frm] + 1
                    queue.append(to)

        return self.distance_from_start[goal] != -1

    def dfs(self, current, goal, flow):
        """
        make flow from `current` to `goal`
        update: capacity of edges, iteration_count
        return: flow (if impossible: 0)
        """
        if current == goal:
            return flow
        i = self.itertion_count[current]
        while self.itertion_count[current] < len(self.edges[current]):
            to = self.edges_index[current][i]
            capacity = self.edges[current][to]
            if capacity > 0 and self.distance_from_start[current] < self.distance_from_start[to]:
                d = self.dfs(to, goal, min(flow, capacity))
                if d > 0:
                    self.edges[current][to] -= d
                    self.edges[to][current] += d
                    return d
            self.itertion_count[current] += 1
            i += 1
        return 0

    def max_flow(self, start, goal):
        """
        return: max flow from `start` to `goal`
        """
        INF = 9223372036854775807
        flow = 0
        self.edges_index = {
            frm: list(self.edges[frm]) for frm in self.edges
        }
        while self.bfs(start, goal):
            self.itertion_count = [0] * self.numVertex
            f = self.dfs(start, goal, INF)
            while f > 0:
                flow += f
                f = self.dfs(start, goal, INF)
        return flow

# end of libs/dinic_maxflow.py
# included from snippets/main.py


def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve_MLE(H, W, world):
    INF = 9223372036854775807
    CHAR_S, CHAR_T, CHAR_O = b"STo"
    leaf = set()
    for pos in world.allPosition():
        if world.mapdata[pos] == CHAR_S:
            start = pos
        if world.mapdata[pos] == CHAR_T:
            goal = pos
        if world.mapdata[pos] == CHAR_O:
            leaf.add(pos)

    sy, sx = divmod(start, W)
    gy, gx = divmod(goal, W)
    if sy == gy or sx == gx:
        return -1

    INF = 100
    d = Dinic(H * W * 2)
    for pos in leaf:
        pos2 = pos + H * W
        d.add_edge(pos, pos2, 1)
        y, x = divmod(pos, W)
        for nx in range(W):
            pos3 = y * W + nx
            if pos3 in leaf:
                d.add_edge(pos2, pos3, INF)
        for ny in range(H):
            pos3 = ny * W + x
            if pos3 in leaf:
                d.add_edge(pos2, pos3, INF)
        
    for nx in range(W):
        spos = sy * W + nx
        if spos in leaf:
            d.add_edge(start, spos, INF)
        gpos = gy * W + nx
        if gpos in leaf:
            d.add_edge(gpos + H * W, goal, INF)
    for ny in range(H):
        spos = ny * W + sx
        if spos in leaf:
            d.add_edge(start, spos, INF)
        gpos = ny * W + gx
        if gpos in leaf:
            d.add_edge(gpos + H * W, goal, INF)

    # debug(d.print_edges(), msg=":d.edges")

    ret = d.max_flow(start, goal)
    # if ret == 101:
    #     debug(d.print_edges(), msg=":d.edges")
    return ret

def solve(H, W, world):
    CHAR_S, CHAR_T, CHAR_O = b"STo"
    leaf = set()
    for pos in world.allPosition():
        if world.mapdata[pos] == CHAR_S:
            start = pos
        if world.mapdata[pos] == CHAR_T:
            goal = pos
        if world.mapdata[pos] == CHAR_O:
            leaf.add(pos)

    sy, sx = divmod(start, W)
    gy, gx = divmod(goal, W)
    if sy == gy or sx == gx:
        return -1

    INF = 10000
    d = Dinic(H * W * 2 + H + W)
    O_BG = H * W
    O_Y = H * W * 2
    O_X = H * W * 2 + H
    for pos in leaf:
        pos2 = pos + O_BG
        d.add_edge(pos, pos2, 1)
        y, x = divmod(pos, W)
        d.add_edge(pos2, y + O_Y, INF)
        d.add_edge(pos2, x + O_X, INF)
        d.add_edge(y + O_Y, pos, INF)
        d.add_edge(x + O_X, pos, INF)

    d.add_edge(start, sy + O_Y, INF)
    d.add_edge(start, sx + O_X, INF)
    d.add_edge(gy + O_Y, goal, INF)
    d.add_edge(gx + O_X, goal, INF)

    ret = d.max_flow(start, goal)
    return ret


def main():
    H, W = map(int, input().split())
    world = OneDimensionMap(H, W)

    print(solve(H, W, world))


# tests
T1 = """
3 3
S.o
.o.
o.T
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
2
"""
T2 = """
3 4
S...
.oo.
...T
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
0
"""
T3 = """
4 3
.S.
.o.
.o.
.T.
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
-1
"""
T4 = """
10 10
.o...o..o.
....o.....
....oo.oo.
..oooo..o.
....oo....
..o..o....
o..o....So
o....T....
....o.....
........oo
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
5
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
