# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, M, edges):
    vlabel = [None] * N
    stack = [(0, None, None)]
    while stack:
        cur, parentEdge, exclude = stack.pop()
        if vlabel[cur] is not None:
            continue
        if parentEdge is None:
            vlabel[cur] = -1  # temporary show "visited"
            used = [False] * N
            if exclude is not None:
                used[exclude - 1] = True
            for child in edges[cur]:
                if vlabel[child]:
                    continue
                c = edges[cur][child]
                stack.append((child, c, None))
                used[c - 1] = True
            vlabel[cur] = used.index(False) + 1
        else:
            vlabel[cur] = parentEdge
            for child in edges[cur]:
                if vlabel[child]:
                    continue
                c = edges[cur][child]
                if c != parentEdge:
                    stack.append((child, c, None))
                else:
                    stack.append((child, c, parentEdge))

    return vlabel


def main():
    N, M = map(int, input().split())
    from collections import defaultdict
    edges = defaultdict(dict)
    for _i in range(M):
        frm, to, cost = map(int, input().split())
        edges[frm-1][to-1] = cost  # -1 for 1-origin vertexes
        edges[to-1][frm-1] = cost  # if bidirectional
    print(*solve(N, M, edges), sep="\n")


# tests
T1 = """
3 4
1 2 1
2 3 2
3 1 3
1 3 1
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
2
1
2
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
