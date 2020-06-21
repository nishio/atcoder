N, Q = [int(x) for x in input().split()]
parent = [-1] * N
rank = [0] * N


def find_root(x):
    p = parent[x]
    if p == -1:
        return x
    p2 = find_root(p)
    parent[x] = p2
    return p2


def unite(x, y):
    x = find_root(x)
    y = find_root(y)
    if x == y:
        return  # already united
    if rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1


def is_connected(x, y):
    return (find_root(x) == find_root(y))


for q in range(Q):
    typ, u, v = [int(x) for x in input().split()]
    if typ == 0:
        unite(u, v)
    else:
        print(1 if is_connected(u, v) else 0)
