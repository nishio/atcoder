# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main_WA():
    N = int(input())
    AS = list(map(int, input().split()))
    SS = [f"{x:030b}" for x in AS]

    start = 1
    end = N - 1
    for i in range(30):
        c = "".join(a[i] for a in SS)
        # debug(c, msg=":c")
        if c.count("1") >= 2:
            s = c.find("1") + 1
            e = c.rfind("1")
            # debug(s, e, start, end, msg=":s, e, start, end")
            if not(e < start or end < s):
                start = max(start, s)
                end = min(end, e)
                # debug(start, end, msg=":start, end")

    x = 0
    for a in AS[:start]:
        x |= a
    y = 0
    for a in AS[start:]:
        y |= a
    print(x ^ y)    
    

def main():
    N = int(input())
    AS = list(map(int, input().split()))

    ret = INF = 9223372036854775807
    for i in range(1, N):
        # debug(AS[:i], AS[i:], msg=":AS[:i], AS[i:]")
        x = 0
        for a in AS[:i]:
            x |= a
        y = 0
        for a in AS[i:]:
            y |= a
        # debug(i, x ^ y, msg=":i, x ^ y")
        ret = min(ret, x ^ y)
    print(ret)

# tests
T1 = """
3
1 5 7
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
2
"""
T2 = """
3
10 10 10
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
0
"""
T3 = """
4
1 3 3 1
"""
TEST_T3 = """
>>> as_input(T3)
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