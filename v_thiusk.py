# derived from https://atcoder.jp/contests/dp/submissions/14624575

from collections import deque


def resolve():
    N, MOD = map(int, input().split())
    edges = [[] for i in range(N)]
    for i in range(N - 1):
        x, y = map(lambda x: int(x)-1, input().split())
        edges[x].append(y)
        edges[y].append(x)
    # vertex 0-origin

    parent = [-1] * N  # what?
    q = deque([0])
    bfs_visited_order = []
    while q:
        i = q.popleft()
        bfs_visited_order.append(i)
        for v in edges[i]:
            if v != parent[i]:
                parent[v] = i
                edges[v].remove(i)
                q.append(v)

    unit = 1  # 単位元
    def merge(a, b): return a * b % MOD
    def adj_bottomup(a, i): return a + 1
    def adj_topdown(a, i, p): return a + 1
    # 最終結果。本問では、全部白みたいなのが認められないので、最終結果では1を足さないようにしています。
    def adj_fin(a, i): return a

    # Bottom-Up 部分
    merged_result = [unit] * N
    dp1 = [0] * N
    for i in reversed(bfs_visited_order[1:]):
        dp1[i] = adj_bottomup(merged_result[i], i)
        p = parent[i]
        merged_result[p] = merge(merged_result[p], dp1[i])

    root = bfs_visited_order[0]
    dp1[root] = adj_fin(merged_result[root], root)

    # Top-Down 部分
    topdown_result = [unit] * N
    for i in bfs_visited_order:
        # 左からDP（結果はTDに入れている）
        cur = topdown_result[i]
        for j in edges[i]:
            topdown_result[j] = cur
            cur = merge(cur, dp1[j])
        # 右からDP（結果はacに入れている）
        cur = unit
        for j in edges[i][::-1]:
            topdown_result[j] = adj_topdown(
                merge(topdown_result[j], cur), j, i)
            cur = merge(cur, dp1[j])
            dp1[j] = adj_fin(merge(merged_result[j], topdown_result[j]), j)

    print(*dp1, sep="\n")


if __name__ == "__main__":
    resolve()
