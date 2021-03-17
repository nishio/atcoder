from random import seed
seed(42)

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

# end of libs/dinic_maxflow.py
from random import randint

def solve1(N, CS, M, DS):
    bits = [0] * N
    INF = 9223372036854775807
    ret = -INF
    ret_cut = None
    for s in range(2 ** N):
        x = s
        for i in range(N):
            bits[i] = x % 2
            x >>= 1
        r = 0
        for i in range(N):
            if bits[i]:
                r += 100
                r -= CS[i]
        for i, j, d in DS:
            if bits[i] and not bits[j]:
                r -= d
        if r > ret:
            ret = r
            ret_cut = bits[:]
    return ret, ret_cut

def setup1():
    global N, CS, M, DS
    N = 20
    M = 100
    CS = [randint(1, 200) for i in range(N)]
    DS = []
    used = set()
    for _m in range(M):
        i = randint(0, N - 2)
        j = randint(i + 1, N - 1)
        if (i, j) in used:
            continue
        used.add((i, j))
        DS.append((i, j, randint(1, 200)))


def pretty_timeit(stmt, setup, number=1):
    from statistics import mean, stdev
    import timeit
    xs = timeit.repeat(
        stmt,
        setup=setup,
        globals=globals(),
        number=number,
    )
    def format_sec(sec):
        if sec > 1:
            return f"{sec:.1f} s"
        else:
            return f"{round(sec * 1000)} ms"

    print(
        f"{format_sec(mean(xs))} ± {format_sec(stdev(xs))} per loop", 
        f"(mean ± std. dev. of {len(xs)} runs, {number} loop each) ")

# pretty_timeit("solve1(N, CS, M, DS)", "setup1()")

def solve2(N, CS, M, DS):
    d = Dinic(N + 2)
    start = N
    goal = N + 1
    offset = 0
    for i in range(N):
        c = CS[i] - 100
        if c > 0:
            d.add_edge(i, goal, c)
        elif c < 0:
            c = -c
            offset += c
            d.add_edge(start, i, c)
    for frm, to, c in DS:
        d.add_edge(frm, to, c)

    ret = d.max_flow(start, goal)
    ret = offset - ret
    ret_cut = d.get_cut(start)[:-2]
    return ret, ret_cut

def test1():
    setup1()
    print(N, CS, M, DS)
    x = solve1(N, CS, M, DS)
    y = solve2(N, CS, M, DS)
    print(x, y, x == y)

# pretty_timeit("solve2(N, CS, M, DS)", "setup1()", 100)

def setup2(_N, _M):
    global N, CS, M, DS
    N = _N
    M = _M
    CS = [randint(1, 200) for i in range(N)]
    DS = []
    used = set()
    for _m in range(M):
        i = randint(0, N - 2)
        j = randint(i + 1, N - 1)
        if (i, j) in used:
            continue
        used.add((i, j))
        DS.append((i, j, randint(1, 200)))


# pretty_timeit("solve2(N, CS, M, DS)", "setup2(100, 100)", 1000)

# pretty_timeit("solve2(N, CS, M, DS)", "setup2(10000, 10000)", 1)

#pretty_timeit("solve2(N, CS, M, DS)", "setup2(100000, 100000)", 1)

# for M in range(10000, 1000000 + 1, 10000):
#     print(M)
#     pretty_timeit("solve2(N, CS, M, DS)", f"setup2(10000, {M})", 1)


# data = []
xs = range(10000, 100000 + 1, 10000)
# for N in xs:
#     print(N)
#     pretty_timeit("solve2(N, CS, M, DS)", f"setup2({N}, {N})", 1)

# print(data)
from statistics import mean
import re
data = """
10000
94 ms ± 46 ms per loop (mean ± std. dev. of 7 runs, 1 loop each) 
20000
192 ms ± 39 ms per loop (mean ± std. dev. of 7 runs, 1 loop each) 
30000
275 ms ± 20 ms per loop (mean ± std. dev. of 7 runs, 1 loop each) 
40000
394 ms ± 21 ms per loop (mean ± std. dev. of 7 runs, 1 loop each) 
50000
554 ms ± 45 ms per loop (mean ± std. dev. of 7 runs, 1 loop each) 
60000
632 ms ± 33 ms per loop (mean ± std. dev. of 7 runs, 1 loop each) 
70000
780 ms ± 52 ms per loop (mean ± std. dev. of 7 runs, 1 loop each) 
80000
894 ms ± 68 ms per loop (mean ± std. dev. of 7 runs, 1 loop each) 
90000
1.1 s ± 45 ms per loop (mean ± std. dev. of 7 runs, 1 loop each) 
100000
1.2 s ± 47 ms per loop (mean ± std. dev. of 7 runs, 1 loop each) 
"""
ys = []
for x in re.findall("[0-9.ms ]+[^±]±", data):
    if "ms" in x:
        ys.append(int(x.split()[0]))
    else:
        ys.append(float(x.split()[0]) * 1000)

from matplotlib import pyplot as plt
plt.plot(xs, ys)
plt.show()