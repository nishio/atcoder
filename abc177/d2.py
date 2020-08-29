#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    N, M = map(int, input().split())
    is_head = [True] * N
    from collections import defaultdict
    edges = defaultdict(list)
    for q in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        is_head[b] = False
        edges[a].append(b)

    to_tail = [-1] * N
    visited = [False] * N

    def dfs(x):
        buf = [0]
        visited[x] = True
        for v in edges[x]:
            if visited[v]:
                continue
            ret = to_tail[v]
            if ret == -1:
                ret = dfs(v)
                to_tail[v] = ret
            buf.append(ret)
        return max(buf) + 1

    buf = [1]
    for i in range(N):
        visited = [False] * N
        buf.append(dfs(i))

    # debug(": to_tail", to_tail)
    print(max(buf))


# tests
T1 = """
5 3
1 2
3 4
5 1
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
3
"""

T2 = """
4 10
1 2
2 1
1 2
2 1
1 2
1 3
1 4
2 3
2 4
3 4
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
4
"""

T3 = """
10 4
3 1
4 1
5 9
2 6
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
3
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
