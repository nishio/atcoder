# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, S):
    i = 0
    state = [0]
    ret = N
    while i < N:
        if state[-1] == 0:
            if S[i] == "f":
                state.append(1)
        elif state[-1] == 1:
            if S[i] == "o":
                state[-1] = 2
            elif S[i] == "f":
                state.append(1)
            else:
                state.pop()
        elif state[-1] == 2:
            if S[i] == "x":
                state.pop()
                ret -= 3
            elif S[i] == "f":
                state.append(1)
            else:
                state.pop()
        i += 1
    return ret


def main():
    # parse input
    N = int(input())
    S = input().strip().decode('ascii')
    print(solve(N, S))


# tests
T1 = """
6
icefox
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
3
"""

T2 = """
7
firebox
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
7
"""

T3 = """
48
ffoxoxuvgjyzmehmopfohrupffoxoxfofofoxffoxoxejffo
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
27
"""

T4 = """
6
ffoxox
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
0
"""

T5 = """
6
fofoxx
"""
TEST_T5 = """
>>> as_input(T5)
>>> main()
0
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
