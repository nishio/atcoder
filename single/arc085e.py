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


def solve(SOLVE_PARAMS):
    pass


def main():
    INF = 9223372036854775807
    N = int(input())
    AS = list(map(int, input().split()))
    offset = sum(max(0, x) for x in AS)
    d = Dinic(N + 2)
    start = N
    goal = N + 1
    for i in range(N):
        c = AS[i] 
        if c > 0:
            d.add_edge(i, goal, c)
        else:
            d.add_edge(start, i, -c)
        n = i + 1
        x = 2 * n
        while x <= N:
            d.add_edge(i, x - 1, INF)
            x += n

    print(offset - d.max_flow(start, goal))

# tests
T1 = """
6
1 2 -6 4 5 3
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
12
"""
T2 = """
6
100 -100 -100 -100 100 -100
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
200
"""
T3 = """
5
-1 -2 -3 -4 -5
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
0
"""
T4 = """
2
-1000 100000
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
99000
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