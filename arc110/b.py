# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, T):
    if N == 1:
        if T == "1":
            return 2 * 10 ** 10
        elif T == "0":
            return 10 ** 10

    state = [True, True, True]
    for c in T:
        nextState = [0] * 3
        for i in range(3):
            nextState[i] = state[i - 1] and (c == "011"[i])
        state = nextState
    ret = 0
    for i in range(3):
        if state[i]:
            ret += (3 * 10 ** 10 - ((i - N) % 3 + N)) // 3 + 1
    return ret


def main():
    # parse input
    N = int(input())
    T = input().strip().decode('ascii')
    print(solve(N, T))


# tests
T1 = """
4
1011
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
9999999999
"""

T3 = """
22
1011011011011011011011
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
9999999993
"""

T4 = """
3
110
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
10000000000
"""

T5 = """
3
101
"""
TEST_T5 = """
>>> as_input(T5)
>>> main()
9999999999
"""

T6 = """
2
11
"""
TEST_T6 = """
>>> as_input(T6)
>>> main()
10000000000
"""

T7 = """
2
10
"""
TEST_T7 = """
>>> as_input(T7)
>>> main()
10000000000
"""

T8 = """
2
01
"""
TEST_T8 = """
>>> as_input(T8)
>>> main()
9999999999
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
