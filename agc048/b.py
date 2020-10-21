# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


# included from snippets/debug_indent.py
debug_indent = 0


def debugi(*x):
    import sys
    global debug_indent
    x = list(x)
    indent = 0
    if x[0].startswith("enter") or x[0][0] == ">":
        indent = 1
    if x[0].startswith("leave") or x[0][0] == "<":
        debug_indent -= 1
    x[0] = "  " * debug_indent + x[0]
    print(*x, file=sys.stderr)
    debug_indent += indent

# end of snippets/debug_indent.py


def solve_TLE(N, AS, BS):
    import sys
    sys.setrecursionlimit(10 ** 6)
    INF = sys.maxsize  # float("inf")
    MOD = 10 ** 9 + 7  # 998_244_353

    # score = [-1] * (N * N + N + 10)  # end * N + start
    from collections import defaultdict

    def f(r):
        start, end = r
        if start + 1 > end:
            return 0
        # debugi(">", start, end)
        ret = 0
        for sep in range(start + 1, end, 2):
            child1_end = sep
            child1_start = start + 1
            # r1 = child1_end * N + child1_start
            # if score[r1] < 0:
            #     score[r1] = f(child1_start, child1_end)
            r1 = (child1_start, child1_end)
            s1 = score.get(r1)
            if s1 is None:
                s1 = score[r1] = f(r1)

            child2_end = end
            child2_start = sep + 1
            # r2 = child2_end * N + child2_start
            # if score[r2] < 0:
            #     score[r2] = f(child2_start, child2_end)
            r2 = (child2_start, child2_end)
            s2 = score.get(r2)
            if s2 is None:
                s2 = score[r2] = f(r2)

            # s = score[r1] + score[r2]
            s = s1 + s2
            # debugi("|", start, sep)
            ret = max(
                ret,
                s + AS[start] + AS[sep],
                s + BS[start] + BS[sep],
            )
        # debugi("<", start, end, ret)

        return ret

    score = {}

    return f((0, N))


def solve_RE(N, AS, BS):
    import sys
    sys.setrecursionlimit(10 ** 6)
    INF = sys.maxsize  # float("inf")
    MOD = 10 ** 9 + 7  # 998_244_353

    score = [-1] * (N * N + N + 10)  # end * N + start

    def f(start, end):
        if start + 1 > end:
            return 0
        # debugi(">", start, end)
        ret = 0
        for sep in range(start + 1, end, 2):
            child1_end = sep
            child1_start = start + 1
            r1 = child1_start + child1_end * N
            s1 = score[r1]
            if s1 == -1:
                s1 = score[r1] = f(child1_start, child1_end)

            child2_end = end
            child2_start = sep + 1
            r2 = child2_start + child2_end * N
            s2 = score[r2]
            if s2 == -1:
                s2 = score[r2] = f(child2_start, child2_end)

            # s = score[r1] + score[r2]
            s = s1 + s2
            # debugi("|", start, sep)
            ret = max(
                ret,
                s + AS[start] + AS[sep],
                s + BS[start] + BS[sep],
            )
        # debugi("<", start, end, ret)

        return ret

    return f(0, N)


def solve(N, AS, BS):
    import sys
    sys.setrecursionlimit(10 ** 6)

    score = {}

    def f(start, end):
        if start + 1 > end:
            return 0
        # debugi(">", start, end)
        ret = 0
        for sep in range(start + 1, end, 2):
            child1_end = sep
            child1_start = start + 1
            r1 = child1_start + child1_end * N
            s1 = score.get(r1)
            if s1 is None:
                s1 = score[r1] = f(child1_start, child1_end)

            child2_end = end
            child2_start = sep + 1
            r2 = child2_start + child2_end * N
            s2 = score.get(r2)
            if s2 is None:
                s2 = score[r2] = f(child2_start, child2_end)

            # s = score[r1] + score[r2]
            s = s1 + s2
            # debugi("|", start, sep)
            ret = max(
                ret,
                s + AS[start] + AS[sep],
                s + BS[start] + BS[sep],
            )
        # debugi("<", start, end, ret)

        return ret

    return f(0, N)


def main():
    N = int(input())
    AS = list(map(int, input().split()))
    BS = list(map(int, input().split()))
    print(solve(N, AS, BS))


# tests
T1 = """
4
4 2 3 1
2 3 2 4
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
12
"""

T2 = """
10
866111664 844917655 383133839 353498483 472381277 550309930 378371075 304570952 955719384 705445072
178537096 218662351 231371336 865935868 579910117 62731178 681212831 16537461 267238505 318106937
"""
_TEST_T2 = """
>>> as_input(T2)
>>> main()
6629738472
"""

T3 = """
4
0 1 1 0
1 0 0 1
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
4
"""

T4 = """
6
1 1 0 0 1 1
0 0 1 1 0 0
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
6
"""

T5 = """
6
1 0 0 1 0 0
0 1 1 0 1 1
"""
TEST_T5 = """
>>> as_input(T5)
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
