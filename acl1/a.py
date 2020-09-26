#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)

# Strongly connected component
# derived from https://atcoder.jp/contests/practice2/submissions/16645774


def get_strongly_connected_components(edges, num_vertex):
    """
    edges: [(v1, v2)]
    """
    from collections import defaultdict

    reverse_edges = defaultdict(list)
    for v1 in edges:
        for v2 in edges[v1]:
            reverse_edges[v2].append(v1)

    terminate_order = []
    done = [0] * num_vertex  # 0 -> 1 -> 2
    count = 0
    for i0 in range(num_vertex):
        if done[i0]:
            continue
        queue = [~i0, i0]
        # dfs
        while queue:
            i = queue.pop()
            if i < 0:
                if done[~i] == 2:
                    continue
                done[~i] = 2
                terminate_order.append(~i)
                count += 1
                continue
            if i >= 0:
                if done[i]:
                    continue
                done[i] = 1
            for j in edges[i]:
                if done[j]:
                    continue
                queue.append(~j)
                queue.append(j)

    done = [0] * num_vertex
    result = []
    for i0 in terminate_order[::-1]:
        if done[i0]:
            continue
        component = []
        queue = [~i0, i0]
        while queue:
            i = queue.pop()
            if i < 0:
                if done[~i] == 2:
                    continue
                done[~i] = 2
                component.append(~i)
                continue
            if i >= 0:
                if done[i]:
                    continue
                done[i] = 1
            for j in reverse_edges[i]:
                if done[j]:
                    continue
                queue.append(~j)
                queue.append(j)
        result.append(component)
    return result


def solve(N, edges):
    ret = [0] * N
    scc = get_strongly_connected_components(edges, N)
    for g in scc:
        n = len(g)
        for v in g:
            ret[v] = n

    return ret


def main():
    # parse input
    N = int(input())
    from collections import defaultdict
    edges = defaultdict(list)
    for _i in range(N):
        a, b = map(int, input().split())
        edges[a - 1].append(b - 1)
        edges[b - 1].append(a - 1)

    print(*solve(N, edges), sep="\n")


# tests
T1 = """
4
1 4
2 3
3 1
4 2
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
result
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
