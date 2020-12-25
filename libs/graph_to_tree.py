def graph_to_tree(N, edges, root):
    from collections import defaultdict
    children = defaultdict(list)
    parents = [None] * N
    root = 0
    parents[root] = root
    stack = [root]
    while stack:
        v = stack.pop()
        for u in edges[v]:
            if parents[u] is not None:
                # already visited
                continue
            parents[u] = v
            children[v].append(u)
            stack.append(u)
    return children, parents
