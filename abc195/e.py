# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    N = int(input())
    SS = input().strip().decode('ascii')
    XS = input().strip().decode('ascii')

    goal = [0] * 7
    goal[0] = 1  # if 1 Taka win

    for i in reversed(range(N)):
        s = int(SS[i])
        prev_goal = []
        if XS[i] == "A":
            for prev in range(7):
                if goal[(prev * 10 + s) % 7] == 0 or goal[(prev * 10) % 7] == 0:
                    prev_goal.append(0)
                else:
                    prev_goal.append(1)
        else:  # "T" 
            for prev in range(7):
                if goal[(prev * 10 + s) % 7] == 1 or goal[(prev * 10) % 7] == 1:
                    prev_goal.append(1)
                else:
                    prev_goal.append(0)
        goal = prev_goal

    if goal[0] == 1:
        print("Takahashi")
    else:
        print("Aoki")

# tests
T1 = """
2
35
AT
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
Takahashi
"""
T2 = """
5
12345
AAAAT
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
Aoki
"""
T3 = """
5
67890
TTTTA
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
Takahashi
"""
T4 = """
5
12345
ATATA
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
Aoki
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