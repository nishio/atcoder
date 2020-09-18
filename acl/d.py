#!/usr/bin/env python3
from collections import deque
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7

INF = 10 ** 10


def init():
    global edges
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
    distance_from_start = [-1] * (MAX_VERTEX + 1)
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
    global itertion_count, edges_index, original_edges, MAX_VERTEX
    from copy import deepcopy
    original_edges = deepcopy(edges)
    flow = 0
    edges_index = {
        frm: list(edges[frm]) for frm in edges
    }
    MAX_VERTEX = max(edges) if edges else goal
    while bfs(start, goal):
        itertion_count = [0] * (MAX_VERTEX + 1)
        f = dfs(start, goal, INF)
        while f > 0:
            flow += f
            f = dfs(start, goal, INF)
    return flow


def get_flow():
    result = []
    for v in original_edges:
        for u in original_edges[v]:
            if original_edges[v][u] > 0:
                d = original_edges[v][u] - edges[v][u]
                if d > 0:
                    result.append((v, u, d))
    return result


def debug(*x):
    print(*x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def readMap(H, W, S=1):
    global SENTINEL, HEIGHT, WIDTH
    SENTINEL = S
    HEIGHT = H + SENTINEL * 2
    WIDTH = W + SENTINEL * 2
    data = [0] * (HEIGHT * WIDTH)
    ok = ord(".")
    for i in range(H):
        S = input().strip()
        y = (i + SENTINEL) * WIDTH
        for j in range(W):
            data[y + (j + SENTINEL)] = 1 if S[j] == ok else 0
    return data


def main():
    # parse input
    init()
    N, M = map(int, input().split())
    data = readMap(N, M)
    odd = []
    even = []
    from collections import defaultdict
    tmp_edges = defaultdict(list)
    for i in range(len(data) - WIDTH):
        if not data[i]:
            continue
        y, x = divmod(i, WIDTH)
        if (x + y) % 2:
            odd.append(i)
            isEven = False
        else:
            even.append(i)
            isEven = True
        j = i + 1
        if data[j]:
            if isEven:
                tmp_edges[j].append(i)
            else:
                tmp_edges[i].append(j)

        j = i + WIDTH
        if data[j]:
            if isEven:
                tmp_edges[j].append(i)
            else:
                tmp_edges[i].append(j)

    START = 0
    GOAL = 1
    for v in odd:
        tmp_edges[START].append(v)
    for v in even:
        tmp_edges[v].append(GOAL)

    for v in tmp_edges:
        for u in tmp_edges[v]:
            add_edge(v, u, 1)

    ret = max_flow(START, GOAL)
    print(ret)

    flow = get_flow()
    outmap = ["." if x else "#" for x in data]
    for v, u, _c in flow:
        if v == START:
            continue
        if u == GOAL:
            continue
        if u < v:
            u, v = v, u
        if u - v == 1:
            outmap[u] = "<"
            outmap[v] = ">"
        if u - v == WIDTH:
            outmap[u] = "^"
            outmap[v] = "v"

    for y in range(N):
        start = (y + 1) * WIDTH + SENTINEL
        end = start + M
        print("".join(outmap[start:end]))


# tests
T1 = """
3 3
#..
..#
...
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
3
#><
><#
><.
"""


T2 = """
10 10
.#........
#.#.......
.#........
..........
..........
..........
......#...
..........
..........
..........
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
46
.#><><><><
#.#><><><v
v#><><><v^
^><><><v^v
><><><v^v^
><><><^v^v
><><><#^v^
><><><><^v
><><><><v^
><><><><^.
"""

T3 = """
1 5
.....
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
2
><><.
"""

T4 = """
3 1
.
.
.
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
1
v
^
.
"""

T5 = """
3 1
.
#
.
"""
TEST_T5 = """
>>> as_input(T5)
>>> main()
0
.
#
.
"""

T6 = """
1 3
###
"""
TEST_T6 = """
>>> as_input(T6)
>>> main()
0
###
"""


def _test():
    import doctest
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
            doctest.run_docstring_examples(g[k], g, name=k)


def as_input(s):
    "use in test, use given string as input file"
    import io
    f = io.StringIO(s.strip())
    g = globals()
    g["input"] = lambda: bytes(f.readline(), "ascii")
    g["read"] = lambda: bytes(f.read(), "ascii")


input = sys.stdin.buffer.readline
read = sys.stdin.buffer.read

if sys.argv[-1] == "-t":
    print("testing")
    _test()
    sys.exit()

main()
