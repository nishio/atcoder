# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    N, M = map(int, input().split())
    from collections import defaultdict
    edges = defaultdict(lambda: defaultdict(list))
    for _i in range(M):
        frm, to, letter = input().split()
        frm = int(frm)
        to = int(to)
        edges[frm][letter].append(to)
        edges[to][letter].append(frm)

    from heapq import heappush, heappop
    queue = [(0, (1, N))]
    visited = set()
    while queue:
        cost, pair = heappop(queue)
        # debug(cost, pair, msg=":cost, pair")
        if pair in visited:
            continue
        visited.add(pair)
        frm, to = pair
        if frm == to:
            print(cost * 2)
            return

        for c in edges[to]:
            for x in edges[to][c]:
                if x == frm:
                    print(cost * 2 + 1)
                    return

        for c in edges[frm]:
            for x in edges[to][c]:
                for y in edges[frm][c]:
                    heappush(queue, (cost + 1, (y, x)))

    print(-1)

# tests
T1 = """
8 8
1 2 a
2 3 b
1 3 c
3 4 b
4 5 a
5 6 c
6 7 b
7 8 a
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
10
"""
T2 = """
4 5
1 1 a
1 2 a
2 3 a
3 4 b
4 4 a
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
5
"""
T3 = """
3 4
1 1 a
1 2 a
2 3 b
3 3 b
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
-1
"""
T4 = """
2 1
1 2 a
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
1
"""
T5 = """
2 1
2 1 a
"""
TEST_T5 = """
>>> as_input(T5)
>>> main()
1
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