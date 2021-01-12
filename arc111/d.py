# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    _N, M = map(int, input().split())
    from collections import defaultdict
    edgelist = []
    for _i in range(M):
        frm, to = map(int, input().split())
        edgelist.append((frm - 1, to - 1))

    CS = list(map(int, input().split()))

    answer = {}
    edges = defaultdict(list)
    for v1, v2 in edgelist:
        if CS[v1] > CS[v2]:
            answer[(v1, v2)] = "->"
        elif CS[v1] < CS[v2]:
            answer[(v1, v2)] = "<-"
        else:
            edges[v1].append(v2)
            edges[v2].append(v1)

    for v1, v2 in edgelist:
        if (v1, v2) not in answer:
            stack = [(v1, v2)]
            while stack:
                v1, v2 = stack.pop()
                if (v1, v2) in answer:
                    continue
                answer[(v1, v2)] = "->"
                answer[(v2, v1)] = "<-"
                for v3 in edges[v2]:
                    if v3 == v1:
                        continue
                    stack.append((v2, v3))

    for v1, v2 in edgelist:
        print(answer[(v1, v2)])


# tests
T1 = """
3 3
1 2
2 3
3 1
3 3 3
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
->
->
->
"""

T2 = """
3 2
1 2
2 3
1 2 3
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
<-
<-
"""

T3 = """
6 3
1 2
4 3
5 6
1 2 1 2 2 1
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
<-
->
->
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
