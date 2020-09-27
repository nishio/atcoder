"""
Strongly connected component
derived from https://atcoder.jp/contests/practice2/submissions/16645774
"""


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


def solve(N, D, data):
    # edges = [[] for i in range(N * 2)]
    # edges = []
    from collections import defaultdict
    edges = defaultdict(list)

    def add_then_edge(i, bool_i, j, bool_j):
        edges[i * 2 + int(bool_i)].append(j * 2 + int(bool_j))
        # edges.append((i * 2 + int(bool_i), j * 2 + int(bool_j)))

    for i in range(N):
        xi, yi = data[i]
        for j in range(i + 1, N):
            xj, yj = data[j]
            if abs(xi - xj) < D:
                add_then_edge(i, 0, j, 1)
                add_then_edge(j, 0, i, 1)
            if abs(xi - yj) < D:
                add_then_edge(i, 0, j, 0)
                add_then_edge(j, 1, i, 1)
            if abs(yi - xj) < D:
                add_then_edge(i, 1, j, 1)
                add_then_edge(j, 0, i, 0)
            if abs(yi - yj) < D:
                add_then_edge(i, 1, j, 0)
                add_then_edge(j, 1, i, 0)

    scc = get_strongly_connected_components(edges, N * 2)
    group_id = [0] * (2 * N)
    for i, xs in enumerate(scc):
        for x in xs:
            group_id[x] = i

    ret = [0] * N
    for i in range(N):
        if group_id[2 * i] == group_id[2 * i + 1]:
            print("No")
            return

        ret[i] = (group_id[2 * i] < group_id[2 * i + 1])

    print("Yes")
    for i in range(N):
        print(data[i][ret[i]])


def main():
    # parse input
    N, D = map(int, input().split())
    data = []
    for _i in range(N):
        data.append(tuple(map(int, input().split())))

    solve(N, D, data)


# tests
T1 = """
3 2
1 4
2 5
0 6
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
Yes
4
2
6
"""

T2 = """
3 3
1 4
2 5
0 6
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
No
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
