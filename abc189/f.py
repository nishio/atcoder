# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solveWA(N, M, K, AS):
    setA = set(AS)

    table = [0] * (N + M + 1)
    tableF = [0] * (N + M + 1)
    sumTail = 0.0
    numFuridashi = 0
    sumFuridashi = 0
    for i in range(N - 1, -1, -1):
        if i in setA:
            numFuridashi += 1
            v = 0
        else:
            v = sumTail / M + 1
        if i + M in setA:
            numFuridashi -= 1

        table[i] = v
        tableF[i] = (numFuridashi + sumFuridashi) / M
        sumTail += v - table[i + M]
        sumFuridashi += tableF[i] - tableF[i + M]

    debug(table, msg=":table")
    debug(tableF, msg=":tableF")
    return table[0] / (1 - tableF[0])


def solve(N, M, K, AS):
    setA = set(AS)
    count = 0
    for i in range(N):
        if i in setA:
            count += 1
            if count == M:
                return -1  # unreachable
        else:
            count = 0

    table = [0] * (N + M + 1)
    tableF = [0] * (N + M + 1)
    sumTable = 0
    sumTableF = 0
    for i in range(N - 1, -1, -1):
        if i in setA:
            table[i] = 0
            tableF[i] = 1
        else:
            v = sumTable
            f = sumTableF
            table[i] = v / M + 1
            tableF[i] = f / M

        sumTable += table[i] - table[i + M]
        sumTableF += tableF[i] - tableF[i + M]

    if tableF[0] == 1:
        return -1
    return table[0] / (1 - tableF[0])


def main():
    # parse input
    N, M, K = map(int, input().split())
    AS = list(map(int, input().split()))

    print(solve(N, M, K, AS))


# tests
T1 = """
2 2 0
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
1.5
"""

T2 = """
2 2 1
1
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
2.0
"""

T3 = """
100 6 10
11 12 13 14 15 16 17 18 19 20
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
-1
"""

T4 = """
100000 2 2
2997 92458
"""
_TEST_T4 = """
>>> as_input(T4)
>>> main()
201932.2222
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
