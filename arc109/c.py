# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def naive(N, K, S):
    X0 = [0 if c == "R" else 1 if c == "P" else 2 for c in S]
    match = [0, 1, 0, 1, 1, 2, 0, 2, 2]

    last = X0
    next = []
    for i in range(0, 2 ** K, 2):
        next.append(match[last[i % N] * 3 + last[(i + 1) % N]])
    # debug(next, msg=":next")
    last = next
    while next:
        next = []
        n = len(last)
        for i in range(0, n, 2):
            next.append(match[last[i % n] * 3 + last[(i + 1) % n]])
        # debug(next, msg=":next")
        if len(next) == 1:
            return "RPS"[next[0]]
        last = next


def solve(N, K, S):
    X0 = [0 if c == "R" else 1 if c == "P" else 2 for c in S]
    match = [0, 1, 0, 1, 1, 2, 0, 2, 2]

    last = X0
    next = []
    for i in range(0, 4 * N, 2):
        next.append(match[last[i % N] * 3 + last[(i + 1) % N]])
    # debug(next, msg=":next")
    last = next
    for k in range(K - 1, 0, -1):
        next = []
        n = 2 * N
        for i in range(0, 4 * N, 2):
            next.append(match[last[i % n] * 3 + last[(i + 1) % n]])
        # debug(next, msg=":next")
        last = next
    return "RPS"[last[0]]


def main():
    # parse input
    N, K = map(int, input().split())
    S = input().strip().decode('ascii')
    print(solve(N, K, S))


# tests
T1 = """
3 2
RPS
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
P
"""

T2 = """
11 1
RPSSPRSPPRS
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
P
"""

T3 = """
1 100
S
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
S
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
