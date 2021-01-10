# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(X, Y):
    from heapq import heappush, heappop

    queue = [(0, Y)]
    minCost = {Y: 0}
    INF = 9223372036854775807

    def add(cost, y):
        c = minCost.get(y, INF)
        if cost < c:
            minCost[y] = cost
            heappush(queue, (cost, y))

    while True:
        cost, y = heappop(queue)
        if y == X:
            return cost
        if y < X:
            add(cost + (X - y), X)
            continue
        if y == X + 1:
            add(cost + 1, X)
            continue

        add(cost + (y - X), X)

        if y % 2 == 0:
            add(cost + 1, y // 2)
        else:
            add(cost + 2, (y + 1) // 2)
            add(cost + 2, (y - 1) // 2)


def main():
    X, Y = map(int, input().split())
    print(solve(X, Y))


def blute(X, Y):
    queue = {X}
    ret = 0
    while True:
        newqueue = set()
        if Y in queue:
            return ret
        ret += 1
        for x in queue:
            newqueue.add(x * 2)
            newqueue.add(x + 1)
            newqueue.add(x - 1)
        queue = newqueue


def fulltest():
    for x in range(20):
        for y in range(20):
            s = solve(x, y)
            b = blute(x, y)
            if s != b:
                print(x, y, s, b)


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

T5 = """
1 12
"""
TEST_T5 = """
>>> as_input(T5)
>>> main()
4
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
