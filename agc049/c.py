# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, AS, BS):
    NGs = []
    spans = []
    for i in range(N):
        if BS[i] >= AS[i]:
            NGs.append(AS[i])
        spans.append((AS[i] - BS[i], +1))
        spans.append((AS[i] - 1, -1))

    spans.sort()
    # debug(spans, msg=":spans")
    i = 0
    cover = 0
    ret = 0
    for pos, diff in spans:
        # debug(pos, diff, msg=":pos, diff")
        if pos > NGs[i]:
            # debug(NGs[i], msg=":NGs[i]")
            if cover > 0:
                # debug(cover, msg=":cover")
                # already covered
                pass
            else:
                ret += 1
            i += 1
            if i == len(NGs):
                break
        cover += diff

    return ret


def main():
    # parse input
    N = int(input())
    AS = list(map(int, input().split()))
    BS = list(map(int, input().split()))
    print(solve(N, AS, BS))


# tests
T1 = """
3
1 2 3
1 2 1
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
1
"""

T2 = """
4
1 3 5 7
3 1 4 1
"""
TEST_T2 = """
>>> as_input(T2)
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
