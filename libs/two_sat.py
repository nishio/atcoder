"""
Two SAT
derived from https://atcoder.jp/contests/practice2/submissions/16645774

usage:
    from collections import defaultdict
    edges = defaultdict(list)

    add_then_edge(edges, i, 0, j, 1)
    add_or_edge(edges, j, 0, i, 1)

    scc = get_strongly_connected_components(edges, N * 2)
    ret = get_sat_result(scc, N * 2)
    if ret is None:
        print("No")
        return
    print(ret)
"""


def get_strongly_connected_components(edges, num_vertex):
    """
    edges: {v1: [v2, v3]]}
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


def add_then_edge(edges, i, bool_i, j, bool_j):
    edges[i * 2 + int(bool_i)].append(j * 2 + int(bool_j))


def add_or_edge(edges, i, neg_i, j, neg_j):
    add_then_edge(edges, i, False ^ neg_i, j, True ^ neg_j)
    add_then_edge(edges, j, False ^ neg_j, i, True ^ neg_i)


def get_sat_result(scc, num_vertex):
    group_id = [0] * num_vertex
    for i, xs in enumerate(scc):
        for x in xs:
            group_id[x] = i

    N = num_vertex // 2
    ret = [0] * N
    for i in range(N):
        if group_id[2 * i] == group_id[2 * i + 1]:
            return None  # mean not satisfied

        ret[i] = (group_id[2 * i] < group_id[2 * i + 1])

    return ret

# --- end of library ---


def solve(N, D, data):
    from collections import defaultdict
    edges = defaultdict(list)

    for i in range(N):
        xi, yi = data[i]
        for j in range(i + 1, N):
            xj, yj = data[j]
            if abs(xi - xj) < D:
                add_then_edge(edges, i, 0, j, 1)
                add_then_edge(edges, j, 0, i, 1)
            if abs(xi - yj) < D:
                add_then_edge(edges, i, 0, j, 0)
                add_then_edge(edges, j, 1, i, 1)
            if abs(yi - xj) < D:
                add_then_edge(edges, i, 1, j, 1)
                add_then_edge(edges, j, 0, i, 0)
            if abs(yi - yj) < D:
                add_then_edge(edges, i, 1, j, 0)
                add_then_edge(edges, j, 1, i, 0)

    scc = get_strongly_connected_components(edges, N * 2)
    ret = get_sat_result(scc, N * 2)
    if ret is None:
        print("No")
        return

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


if __name__ == "__main__":
    import sys
    input = sys.stdin.buffer.readline
    read = sys.stdin.buffer.read
    if sys.argv[-1] == "-t":
        print("testing")
        _test()
        sys.exit()
    main()
