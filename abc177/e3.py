#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def precompute():
    maxAS = 1000000
    eratree = [0] * (maxAS + 10)
    for p in range(2, maxAS + 1):
        if eratree[p]:
            continue
        # p is prime
        eratree[p] = p
        x = p * p
        while x <= maxAS:
            if not eratree[x]:
                eratree[x] = p
            x += p

    import pickle
    pickle.dump(eratree, open("eratree.pickle", "wb"))


def solve(N, AS):
    import pickle
    eratree = pickle.load(open("eratree.pickle", "rb"))
    num_division = 0

    from collections import defaultdict
    count = defaultdict(int)
    for a in AS:
        factors = []
        while a > 1:
            d = eratree[a]
            factors.append(d)
            a //= d
            num_division += 1
        # debug(": ", factors)
        for f in set(factors):
            count[f] += 1

    # debug(": num_division", num_division)
    if any(x == N for x in count.values()):
        return "not coprime"
    if any(x >= 2 for x in count.values()):
        return "setwise coprime"
    return "pairwise coprime"


def main():
    # parse input
    N = int(input())
    AS = list(map(int, input().split()))
    print(solve(N, AS))


# tests
T1 = """
3
3 4 5
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
pairwise coprime
"""

T2 = """
3
6 10 15
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
setwise coprime
"""

T3 = """
3
6 10 16
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
not coprime
"""

T4 = """
3
100000 100001 100003
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
pairwise coprime
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

if sys.argv[-1] == 'ONLINE_JUDGE':
    precompute()
elif sys.argv[-1] != "DONTCALL":
    import subprocess
    subprocess.call("pypy3 Main.py DONTCALL", shell=True,
                    stdin=sys.stdin, stdout=sys.stdout)
else:
    main()
