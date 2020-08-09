#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def solve(N, SS):
    from collections import defaultdict
    SS.sort(key=lambda s: -len(s))
    debug(": SS", SS)
    ret = 0
    table = defaultdict(lambda: defaultdict(set))
    shortest = INF
    for i, s in enumerate(SS):
        l = len(s)
        if shortest == INF:
            shortest = l
            table[l][s] = set([i])
        elif shortest == l:
            ret += len(table[l][s])
            table[l][s].add(i)

        elif shortest > l:
            # progress DP
            while shortest > l:
                next = shortest - 1
                for k in table[shortest]:
                    v = table[shortest][k]
                    k1 = k[0] + k[2:]
                    table[next][k1] = table[next][k1].union(v)
                    k2 = k[1:]
                    table[next][k2] = table[next][k2].union(v)
                shortest = next
                debug(": table[next]", table[next])
            ret += len(table[l][s])
            table[l][s].add(i)

        else:
            raise NotImplementedError

    return ret


def main():
    # parse input
    N = int(input())
    SS = []
    for i in range(N):
        SS.append(input().strip().decode('ascii'))
    print(solve(N, SS))


def f(s):
    from collections import deque
    q = deque([s])
    while q:
        x = q.popleft()
        if len(x) > 1:
            q.append(x[0] + x[2:])
            q.append(x[1:])
        print(x)


# tests
T1 = """
3
abcxyx
cyx
abc
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
1
"""

T2 = """
6
b
a
abc
c
d
ab
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
5
"""


def _test():
    import doctest
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
            doctest.run_docstring_examples(g[k], g)


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
