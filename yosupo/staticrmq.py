"""
Static RMQ
"""
N, Q = [int(x) for x in input().split()]
AS = [int(x) for x in input().split()]

INF = 10 ** 10
SEG_TREE_WIDTH = 1 << N.bit_length()
seg = [INF] * (SEG_TREE_WIDTH * 2)  # 0-origin


def range_min_query(start, end, node=1, nstart=0, nend=SEG_TREE_WIDTH):
    # print("node", node, (nstart, nend))
    if end < nstart or nend <= start:
        # print("no overlap")
        return INF
    if node >= SEG_TREE_WIDTH:
        # print("leaf")
        return seg[node]
    if start <= nstart and nend < end:
        # print("perfect overlap")
        return seg[node]

    # print("to visit children", node * 2, node * 2 + 1)
    return min(
        range_min_query(start, end, node * 2, nstart, (nstart + nend) // 2),
        range_min_query(start, end, node * 2 + 1, (nstart + nend) // 2, nend),
    )


for i, x in enumerate(AS):
    seg[SEG_TREE_WIDTH + i] = x

for i in reversed(range(SEG_TREE_WIDTH)):
    seg[i] = min(seg[i * 2], seg[i * 2 + 1])


for q in range(Q):
    l, r = [int(x) for x in input().split()]
    # print(l, r)
    print(range_min_query(l, r-1))
