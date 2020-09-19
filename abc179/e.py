#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def loop():
    xs = [3, 1, 2, 1]
    ret = []
    N = 6
    visited = [0] * 100
    for i, a in enumerate(xs):
        if visited[a]:
            debug("ret", ret)
            debug("visited", visited)
            s = sum(ret)
            loop_start = visited[a] - 1
            debug("a, visited[a], i", a, visited[a], i)
            loop_end = i
            loop_sum = sum(ret[loop_start:loop_end])
            debug("loop_sum", loop_sum)
            loop_length = loop_end - loop_start
            loop_count = (N - i) // loop_length
            debug("loop_count", loop_count)
            debug("(N - i) % loop_length", (N - i) % loop_length)
            loop_left = (N - i) % loop_length
            loop_tail = sum(ret[loop_start:loop_start + loop_left])
            debug("loop_tail", loop_tail)
            return s + (N - i) // loop_length * loop_sum + loop_tail
        ret.append(a)
        visited[a] = (i + 1)


def solve(N, X, M):
    visited = [0] * M
    a = X
    ret = []
    for i in range(N):
        if visited[a]:
            # debug("ret", ret)
            s = sum(ret)
            loop_start = visited[a] - 1
            # debug("a, visited[a], i", a, visited[a], i)
            loop_end = i
            loop_sum = sum(ret[loop_start:loop_end])
            # debug("loop_sum", loop_sum)
            loop_length = loop_end - loop_start
            loop_count = (N - i) // loop_length
            # debug("loop_count", loop_count)
            # debug("(N - i) % loop_length", (N - i) % loop_length)
            loop_left = (N - i) % loop_length
            loop_tail = sum(ret[loop_start:loop_start + loop_left])
            # debug("loop_tail", loop_tail)
            return s + loop_count * loop_sum + loop_tail
        ret.append(a)
        visited[a] = (i + 1)
        a = (a * a) % M

    return sum(ret)


def main():
    # parse input
    N, X, M = map(int, input().split())
    print(solve(N, X, M))


# tests
T1 = """
6 2 1001
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
1369
"""

T2 = """
1000 2 16
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
6
"""

T3 = """
10000000000 10 99959
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
492443256176507
"""


def _test():
    import doctest
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
            doctest.run_docstring_examples(g[k], g, name=k)


def as_input(s):
    "use in test, use given string as input file"
    import io
    f = io.StringIO(s.strip())
    g = globals()
    g["input"] = lambda: bytes(f.readline(), "ascii")
    g["read"] = lambda: bytes(f.read(), "ascii")


input = sys.stdin.buffer.readline
read = sys.stdin.buffer.read

if sys.argv[-1] == "-t":
    print("testing")
    _test()
    sys.exit()

main()
