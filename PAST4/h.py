# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, M, K, data):
    from collections import Counter
    ret = 1
    for y in range(N):
        for x in range(M):
            for w in range(ret + 1, min(N - y + 1, M - x + 1)):
                # debug(x, y, w, msg=":x, y, w")
                c = Counter(data[y + i][x + j]
                            for i in range(w)
                            for j in range(w))

                mc = c.most_common(1)[0][1]
                if mc + K >= w * w:
                    ret = w

    return ret


def main():
    # parse input
    N, M, K = map(int, input().split())
    data = []
    for _i in range(N):
        line = input().strip()
        data.append([x - ord("0") for x in line])

    print(solve(N, M, K, data))


# tests
T1 = """
3 4 3
1123
1214
1810
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
3
"""

T2 = """
8 6 40
846444
790187
264253
967004
578258
204367
681998
034243
"""
TEST_T2 = """
>>> as_input(T2)
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
