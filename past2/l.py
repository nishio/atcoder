# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, K, D, AS):
    from heapq import heappush, heappop, heapify
    end = N - D * (K - 1)
    start = 0
    ret = []
    queue = [(AS[i], i) for i in range(start, end)]
    heapify(queue)
    for _i in range(K):
        if start >= end:
            return [-1]
        while True:
            v, i = heappop(queue)
            if start <= i < end:
                break
        ret.append(v)
        start = i + D
        for i in range(end, min(end + D, N)):
            heappush(queue, (AS[i], i))
        end += D
    return ret


def main():
    N, K, D = map(int, input().split())
    AS = list(map(int, input().split()))
    print(*solve(N, K, D, AS))


# tests
T1 = """
3 2 2
3 1 4
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
3 4
"""

T2 = """
3 3 2
3 1 4
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
-1
"""

T3 = """
3 2 1
3 1 4
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
1 4
"""

T4 = """
4 2 2
3 6 5 5
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
3 5
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
