
# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, K, S):
    if 0 in S:
        return N

    start = 0
    result = 0
    end = 1
    prod = S[start]
    while end < N:
        if prod > K:
            prod = prod * S[end] // S[start]
            start += 1
            end += 1
        else:
            result += 1
            prod = prod * S[end]
            end += 1
    if prod <= K:
        result += 1

    return result


def solve(N, K, S):
    if 0 in S:
        return N
    if K == 0:
        return 0

    start = 0
    result = 0
    end = 1
    prod = S[start]
    while end < N:
        if prod <= K:
            result = max(result, end - start)
            prod = prod * S[end]
            end += 1
        else:
            prod = prod // S[start]
            start += 1
    if prod <= K:
        result = max(result, end - start)

    return result


def main():
    # parse input
    N, K = map(int, input().split())
    S = []
    for _i in range(N):
        S.append(int(input()))
    print(solve(N, K, S))


# tests
T1 = """
7 6
4
3
1
1
2
10
2
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
4
"""

T2 = """
6 10
10
10
10
10
0
10
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
6
"""

T3 = """
6 9
10
10
10
10
10
10
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
0
"""

T4 = """
4 0
1
2
3
4
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
0
"""

T5 = """
5 1
1
1
1
2
1
"""
TEST_T5 = """
>>> as_input(T5)
>>> main()
3
"""

T6 = """
3 1
1
1
1
"""
TEST_T6 = """
>>> as_input(T6)
>>> main()
3
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

# end of snippets/main.py
