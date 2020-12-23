# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, AS):
    ranks = [1] * (2 ** N)
    winner = list(range(2 ** N))
    next_rank = 2

    while len(winner) > 2:
        next_winner = []
        for i in range(0, len(winner), 2):
            a = winner[i]
            b = winner[i + 1]
            if AS[a] > AS[b]:
                next_winner.append(a)
                ranks[a] = next_rank
            else:
                next_winner.append(b)
                ranks[b] = next_rank
        winner = next_winner
        next_rank += 1
    return ranks


def main():
    # parse input
    N = int(input())
    AS = list(map(int, input().split()))
    print(*solve(N, AS), sep="\n")


# tests
T1 = """
2
2 4 3 1
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
1
2
2
1
"""

T2 = """
1
2 1
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
1
1
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
