# included from libs/mincostflow.py
"""
Min Cost Flow

"""

# derived: https://atcoder.jp/contests/practice2/submissions/16726003
from heapq import heappush, heappop


class MinCostFlow():
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.pos = []

    def add_edge(self, fr, to, cap, cost):
        #assert 0 <= fr < self.n
        #assert 0 <= to < self.n
        m = len(self.pos)
        self.pos.append((fr, len(self.graph[fr])))
        self.graph[fr].append([to, len(self.graph[to]), cap, cost])
        self.graph[to].append([fr, len(self.graph[fr]) - 1, 0, -cost])
        return m

    def get_edge(self, idx):
        #assert 0 <= idx < len(self.pos)
        to, rev, cap, cost = self.graph[self.pos[idx][0]][self.pos[idx][1]]
        _rev_to, _rev_rev, rev_cap, _rev_cost = self.graph[to][rev]
        return self.pos[idx][0], to, cap + rev_cap, rev_cap, cost

    def edges(self):
        for i in range(len(self.pos)):
            yield self.get_edge(i)

    def dual_ref(self, s, t):
        dist = [2**63 - 1] * self.n
        dist[s] = 0
        vis = [0] * self.n
        self.pv = [-1] * self.n
        self.pe = [-1] * self.n
        queue = []
        heappush(queue, (0, s))
        while queue:
            k, v = heappop(queue)
            if vis[v]:
                continue
            vis[v] = True
            if v == t:
                break
            for i in range(len(self.graph[v])):
                to, _rev, cap, cost = self.graph[v][i]
                if vis[to] or cap == 0:
                    continue
                cost += self.dual[v] - self.dual[to]
                if dist[to] - dist[v] > cost:
                    dist[to] = dist[v] + cost
                    self.pv[to] = v
                    self.pe[to] = i
                    heappush(queue, (dist[to], to))
        if not vis[t]:
            return False
        for v in range(self.n):
            if not vis[v]:
                continue
            self.dual[v] -= dist[t] - dist[v]
        return True

    def flow(self, s, t):
        return self.flow_with_limit(s, t, 2**63 - 1)

    def flow_with_limit(self, s, t, limit):
        return self.slope_with_limit(s, t, limit)[-1]

    def slope(self, s, t):
        return self.slope_with_limit(s, t, 2**63 - 1)

    def slope_with_limit(self, s, t, limit):
        #assert 0 <= s < self.n
        #assert 0 <= t < self.n
        #assert s != t
        flow = 0
        cost = 0
        prev_cost = -1
        res = [(flow, cost)]
        self.dual = [0] * self.n
        while flow < limit:
            if not self.dual_ref(s, t):
                break
            c = limit - flow
            v = t
            while v != s:
                c = min(c, self.graph[self.pv[v]][self.pe[v]][2])
                v = self.pv[v]
            v = t
            while v != s:
                _to, rev, _cap, _ = self.graph[self.pv[v]][self.pe[v]]
                self.graph[self.pv[v]][self.pe[v]][2] -= c
                self.graph[v][rev][2] += c
                v = self.pv[v]
            d = -self.dual[s]
            flow += c
            cost += c * d
            if prev_cost == d:
                res.pop()
            res.append((flow, cost))
            prev_cost = cost
        return res


# end of libs/mincostflow.py

# included from snippets/main.py


def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, M, AS, BS, RS):
    global mcf
    INF = 10 ** 5
    mcf = MinCostFlow(N + 5)
    start = N
    goal = N + 1
    round = N + 2
    for i in range(3):
        mcf.add_edge(start, round + i, M, 0)

    for i in range(3):
        for j in range(N):
            r = AS[j] * (BS[j] ** (i + 1)) % RS[i]
            mcf.add_edge(round + i, j, 1, INF - r)

    for j in range(N):
        cs = [AS[j] * (BS[j] ** (k + 1)) for k in range(3)]
        cs.append(0)
        for k in range(3):
            c = cs[k] - cs[k-1]
            mcf.add_edge(j, goal, 1, c)

    return INF * (3 * M) - mcf.flow(start, goal)[-1]


def main():
    # parse input
    N, M = map(int, input().split())
    AS = list(map(int, input().split()))
    BS = list(map(int, input().split()))
    RS = list(map(int, input().split()))
    print(solve(N, M, AS, BS, RS))


# tests
T1 = """
2 1
3 2
3 3
100000 100000 100000
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
81
"""

T2 = """
4 2
2 4 3 3
4 2 3 3
100000 100000 100000
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
210
"""

T3 = """
20 19
3 2 3 4 3 3 2 3 2 2 3 3 4 3 2 4 4 3 3 4
2 3 4 2 4 3 3 2 4 2 4 3 3 2 3 4 4 4 2 2
3 4 5
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
-1417
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
