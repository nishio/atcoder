# included from libs/scc.py
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

# end of libs/scc.py
# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    N = int(input())
    XS = list(map(int, input().split()))
    from collections import defaultdict
    edges = defaultdict(list)
    for i in range(N):
        edges[i].append(XS[i] - 1)

    scc = get_strongly_connected_components(edges, N)
    num_loop = 0
    for s in scc:
        if edges[s[0]][0] in s:
            num_loop += 1
    MOD = 998_244_353
    print((pow(2, num_loop, MOD) - 1) % MOD)

# tests
T1 = """
2
2 1
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
1
"""
T2 = """
2
1 1
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
1
"""
T3 = """
3
1 2 3
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
7
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