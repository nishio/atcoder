# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, S):
    # print(S)
    spaces = []
    if S[0] == ord("#"):
        spaces.append(0)
        state = "BLOCK"
    else:
        state = "SPACE"
    c = 0

    for i in range(N):
        # print(S[i], state)
        if state == "SPACE":
            if S[i] == ord("."):
                c += 1
            else:
                spaces.append(c)
                state = "BLOCK"
        else:
            if S[i] == ord("."):
                state = "SPACE"
                c = 1
            else:
                pass
    if state == "BLOCK":
        spaces.append(0)
    else:
        spaces.append(c)

    # debug(spaces, msg=":spaces")
    m = max(spaces)
    if m > spaces[0] + spaces[-1]:
        print(spaces[0], m - spaces[0])
    else:
        print(spaces[0], spaces[-1])


def main():
    # parse input
    N = int(input())
    S = input().strip()
    solve(N, S)


# tests
T1 = """
5
.#..#
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
1 1
"""

T2 = """
6
..#...
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
2 3
"""

T3 = """
3
###
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
0 0
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
