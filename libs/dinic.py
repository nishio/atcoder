"""
Dinic: MaxFlow
"""

from collections import defaultdict
from collections import deque
INF = 10 ** 10
edges = defaultdict(dict)


def add_edge(frm, to, capacity):
    edges[frm][to] = capacity
    edges[to][frm] = 0


def bfs(start, goal):
    """
    update: distance_from_start
    return bool: can reach to goal
    """
    global distance_from_start
    distance_from_start = [-1] * len(edges)
    queue = deque()
    distance_from_start[start] = 0
    queue.append(start)
    while queue and distance_from_start[goal] == -1:
        frm = queue.popleft()
        for to in edges[frm]:
            if edges[frm][to] > 0 and distance_from_start[to] == -1:
                distance_from_start[to] = distance_from_start[frm] + 1
                queue.append(to)

    return distance_from_start[goal] != -1


def dfs(current, goal, flow):
    """
    make flow from `current` to `goal`
    update: capacity of edges, iteration_count
    return: flow (if impossible: 0)
    """
    if current == goal:
        return flow
    i = itertion_count[current]
    while itertion_count[current] < len(edges[current]):
        to = edges_index[current][i]
        capacity = edges[current][to]
        if capacity > 0 and distance_from_start[current] < distance_from_start[to]:
            d = dfs(to, goal, min(flow, capacity))
            if d > 0:
                edges[current][to] -= d
                edges[to][current] += d
                return d
        itertion_count[current] += 1
        i += 1
    return 0


def max_flow(start, goal):
    """
    return: max flow from `start` to `goal`
    """
    global itertion_count, edges_index
    flow = 0
    edges_index = {
        frm: list(edges[frm]) for frm in edges
    }
    while bfs(start, goal):
        itertion_count = [0] * len(edges)
        f = dfs(start, goal, INF)
        while f > 0:
            flow += f
            f = dfs(start, goal, INF)
    return flow

# --- end of library ---


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
    global read, input
    f = io.StringIO(s.strip())

    def input():
        return bytes(f.readline(), "ascii")

    def read():
        return bytes(f.read(), "ascii")


if __name__ == "__main__":
    import sys
    if sys.argv[-1] == "-t":
        print("testing")
        _test()
        sys.exit()
    main()
