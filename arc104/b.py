# included from snippets/main.py
def debug(*x):
    import sys
    print(*x, file=sys.stderr)


def solve_simple(N, S):
    from collections import Counter
    ret = 0
    for i in range(N):
        for j in range(i + 1, N + 1):
            subseq = S[i:j]
            debug("subseq", subseq)
            count = Counter(subseq)
            if count["A"] == count["T"] and count["C"] == count["G"]:
                ret += 1
    return ret


def solve(N, S):
    from collections import defaultdict
    ret = 0
    for i in range(N):
        count = defaultdict(int)
        for j in range(i, N):
            count[S[j]] += 1
            if count["A"] == count["T"] and count["C"] == count["G"]:
                ret += 1
    return ret


def main():
    # parse input
    N, S = input().split()
    N = int(N)
    S = S.strip().decode('ascii')
    print(solve(N, S))


# tests
T1 = """
4 AGCT
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
2
"""

T2 = """
4 ATAT
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
4
"""

T3 = """
10 AAATACCGCG
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
6
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
    if sys.argv[-1] == "-t":
        print("testing")
        _test()
        sys.exit()
    main()

# end of snippets/main.py
