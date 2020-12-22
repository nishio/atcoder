# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, M, SS, CS):
    INF = 9223372036854775807
    table = [INF] * (2 ** N)
    table[0] = 0
    SS = [int(s.replace("Y", "1").replace("N", "0"), 2) for s in SS]
    for i in range(M):
        s = SS[i]
        for src in range(2 ** N):
            dst = s | src
            table[dst] = min(table[dst], table[src] + CS[i])
    ret = table[2 ** N - 1]
    if ret == INF:
        return -1
    return ret


def main():
    # parse input
    N, M = map(int, input().split())
    SS = []
    CS = []
    for _m in range(M):
        line = input().strip().decode('ascii')
        s, c = line.split()
        c = int(c)
        SS.append(s)
        CS.append(c)
    print(solve(N, M, SS, CS))


# tests
T1 = """
3 4
YYY 100
YYN 20
YNY 10
NYY 25
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
30
"""

T2 = """
5 4
YNNNN 10
NYNNN 10
NNYNN 10
NNNYN 10
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
-1
"""

T3 = """
10 14
YNNYNNNYYN 774472905
YYNNNNNYYY 75967554
NNNNNNNNNN 829389188
NNNNYYNNNN 157257407
YNNYNNYNNN 233604939
NYYNNNNNYY 40099278
NNNNYNNNNN 599672237
NNNYNNNNYY 511018842
NNNYNNYNYN 883299962
NNNNNNNNYN 883093359
NNNNNYNYNY 54742561
NYNNYYYNNY 386272705
NNNNYYNNNN 565075143
NNYNYNNNYN 123300589
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
451747367
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
