# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    # parse input
    from heapq import heappush, heappop
    X, Y = map(int, input().split())
    queue = [(0, Y)]
    visited = {}
    while True:
        cost, y = heappop(queue)
        visited[y] = True
        # debug(cost, y, msg=":cost, y")
        if y == X:
            print(cost)
            return
        if y < X:
            heappush(queue, (cost + (X - y), X))
            continue
        if y - 1 == X:
            heappush(queue, (cost + 1, X))
            continue

        if y % 2 == 0:
            if y // 2 not in visited:
                heappush(queue, (cost + 1, y // 2))
        else:
            if (y + 1) // 2 not in visited:
                heappush(queue, (cost + 2, (y + 1) // 2))
            if (y - 1) // 2 not in visited:
                heappush(queue, (cost + 2, (y - 1) // 2))


# tests
T1 = """
3 9
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
3
"""

T2 = """
7 11
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
3
"""

T3 = """
1000000000000000000 1000000000000000000
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
0
"""

T4 = """
1 1000000000000000000
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
75
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
