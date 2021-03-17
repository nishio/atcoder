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

    def get_cut(self, start):
        """
        return 0/1: can reach from start
        """
        ret = [0] * self.numVertex
        ret[start] = 1
        queue = deque()
        queue.append(start)
        while queue:
            frm = queue.popleft()
            for to in self.edges[frm]:
                if self.edges[frm][to] > 0 and ret[to] == 0:
                    ret[to] = 1
                    queue.append(to)
        return ret



# --- end of library ---
# Verified: https://atcoder.jp/contests/abc193/submissions/20560918
# Verified: arc074d(1 MLE)

def main():
    # Verified: https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/6/GRL_6_A
    V, E = map(int, input().split())
    for _i in range(E):
        v1, v2, capacity = map(int, input().split())
        add_edge(v1, v2, capacity)
    print(max_flow(0, V - 1))


# tests
T1 = """
4 5
0 1 2
0 2 1
1 2 1
1 3 1
2 3 2
"""


def test_T1():
    """
    >>> as_input(T1)
    >>> main()
    3
    """
# add tests above


def _test():
    import doctest
    doctest.testmod()


def as_input(s):
    "use in test, use given string as input file"
    import io
    g = globals()
    f = io.StringIO(s.strip())

    g["input"] = lambda: bytes(f.readline(), "ascii")
    g["read"] = lambda: bytes(f.read(), "ascii")


if __name__ == "__main__":
    import sys
    if sys.argv[-1] == "-t":
        print("testing")
        _test()
        sys.exit()
    main()
