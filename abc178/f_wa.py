#!/usr/bin/env python3
from heapq import heappush, heappop
import sys
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def solve(N, AS, BS):
    acount = [0] * (N + 10)
    bcount = [0] * (N + 10)
    for i in range(N):
        acount[AS[i]] += 1
        bcount[BS[i]] += 1

    overlap = []
    queue = []
    for i in range(N + 10):
        if acount[i] + bcount[i] > N:
            print("No")
            return
        if acount[i] and bcount[i]:
            overlap.append(i)
        if bcount[i]:
            heappush(queue, (- acount[i] - bcount[i], i))

    ret = []
    for i in range(N):
        cx, x = heappop(queue)
        if x == AS[i]:
            # use another number
            try:
                cy, y = heappop(queue)
            except:
                print("No")  # last 10 min. (24 WA)
                return
            ret.append(y)
            bcount[y] -= 1
            if bcount[y]:
                heappush(queue, (cy + 1, y))
            heappush(queue, (cx, x))
        else:
            ret.append(x)
            bcount[x] -= 1
            if bcount[x]:
                heappush(queue, (cx + 1, x))

    print("Yes")
    print(*ret, sep=" ")


def main():
    # parse input
    N = int(input())
    AS = list(map(int, input().split()))
    BS = list(map(int, input().split()))
    solve(N, AS, BS)


# tests
T01 = """
2
1 1
1 1
"""
TEST_T01 = """
>>> as_input(T01)
>>> main()
No
"""

T02 = """
2
1 1
1 2
"""
TEST_T02 = """
>>> as_input(T02)
>>> main()
No
"""

T03 = """
2
1 3
2 3
"""
TEST_T03 = """
>>> as_input(T03)
>>> main()
Yes
3 2
"""

T04 = """
2
1 2
1 3
"""
TEST_T04 = """
>>> as_input(T04)
>>> main()
Yes
3 1
"""

T05 = """
2
1 2
1 2
"""
TEST_T05 = """
>>> as_input(T05)
>>> main()
Yes
2 1
"""

T1 = """
6
1 1 1 2 2 3
1 1 1 2 2 3
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
Yes
2 2 3 1 1 1
"""

T2 = """
5
1 1 2 2 3
1 1 2 2 3
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
result
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
