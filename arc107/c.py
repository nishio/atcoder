# included from snippets/main.py

# included from libs/unionfind.py
"""
Union-Find Tree / Disjoint Set Union (DSU)
"""


def init_unionfind(N):
    global parent, rank, NUM_VERTEX
    NUM_VERTEX = N
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


def num_components():
    return sum(1 for x in range(NUM_VERTEX) if find_root(x) == x)


# end of libs/unionfind.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve_WA(N, K, AS):
    from collections import Counter
    from collections import defaultdict
    MOD = 998_244_353
    init_unionfind(N)
    # debug(AS, msg=":AS")
    for i in range(N):
        for j in range(i + 1, N):
            if all(AS[i][k] + AS[j][k] <= K for k in range(N)):
                unite(i, j)
    ok1 = Counter(find_root(x) for x in range(N)).most_common(1)[0][1]

    same1 = defaultdict(list)
    used = []
    for i in range(N):
        if i in used:
            continue
        for j in range(i + 1, N):
            if all(AS[i][k] == AS[j][k] for k in range(N)):
                same1[i].append(j)
                used.append(j)

    init_unionfind(N)
    for i in range(N):
        for j in range(N):
            if all(AS[k][i] + AS[k][j] <= K for k in range(N)):
                unite(i, j)
    ok2 = Counter(find_root(x) for x in range(N)).most_common(1)[0][1]

    same2 = defaultdict(list)
    used = []
    for i in range(N):
        if i in used:
            continue
        for j in range(i + 1, N):
            if all(AS[k][i] == AS[k][j] for k in range(N)):
                same2[i].append(j)
                used.append(j)

    # debug(ok1, ok2, msg=":ok1, ok2")
    # debug(same1, same2, msg=":same1, same2")
    ret = 1
    for x in range(1, ok1 + 1):
        ret *= x
        ret %= MOD
    for x in range(1, ok2 + 1):
        ret *= x
        ret %= MOD

    div = 1
    for k in same1:
        for x in range(1, len(same1[k]) + 1 + 1):
            div *= x
            div %= MOD
    for k in same2:
        for x in range(1, len(same2[k]) + 1 + 1):
            div *= x
            div %= MOD
    # debug(div, msg=":div")
    div = pow(div, MOD - 2, MOD)

    ret *= div
    ret %= MOD
    return ret


def solve(N, K, AS):
    from collections import Counter
    from collections import defaultdict
    MOD = 998_244_353
    init_unionfind(N)
    for i in range(N):
        for j in range(i + 1, N):
            if all(AS[i][k] + AS[j][k] <= K for k in range(N)):
                unite(i, j)
    ok1 = Counter(find_root(x) for x in range(N)).values()

    init_unionfind(N)
    for i in range(N):
        for j in range(N):
            if all(AS[k][i] + AS[k][j] <= K for k in range(N)):
                unite(i, j)
    ok2 = Counter(find_root(x) for x in range(N)).values()

    ret = 1
    for n in ok1:
        for x in range(1, n + 1):
            ret *= x
            ret %= MOD
    for n in ok2:
        for x in range(1, n + 1):
            ret *= x
            ret %= MOD

    return ret


def main():
    # parse input
    N, K = map(int, input().split())
    AS = []
    for _i in range(N):
        AS.append(list(map(int, input().split())))
    print(solve(N, K, AS))


# tests
T1 = """
3 13
3 2 7
4 8 9
1 6 5
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
12
"""

T2 = """
10 165
82 94 21 65 28 22 61 80 81 79
93 35 59 85 96 1 78 72 43 5
12 15 97 49 69 53 18 73 6 58
60 14 23 19 44 99 64 17 29 67
24 39 56 92 88 7 48 75 36 91
74 16 26 10 40 63 45 76 86 3
9 66 42 84 38 51 25 2 33 41
87 54 57 62 47 31 68 11 83 8
46 27 55 70 52 98 20 77 89 34
32 71 30 50 90 4 37 95 13 100
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
348179577
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
