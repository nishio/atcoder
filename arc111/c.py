# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    N = int(input())
    power = list(map(int, input().split()))
    weight = list(map(int, input().split()))
    package = list(map(int, input().split()))

    to_cont = True
    while to_cont:
        to_cont = False
        for frm in range(N):
            to = package[frm] - 1
            if to == frm:
                continue
            if power[frm] < weight[package[to] - 1]:
                print(frm, to)
                debug(frm, to, msg=":frm, to")
                package[frm], package[to] = package[to], package[frm]
            else:
                to_cont = True


# tests
T1 = """
4
3 4 8 6
5 3 1 3
3 4 2 1
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
result
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
