# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(S, X):
    blocks = []
    buf = []
    blocklen = 0
    prev_blocklen = 0
    bodylength = []
    blocklength = []
    mblocklength = []
    taillength = []
    for c in S:
        if c in "123456789":
            c = int(c) + 1
            blocks.append((blocklen, buf))
            taillength.append(len(buf))
            blocklen += len(buf)
            blocklength.append(blocklen)
            blocklen *= c
            mblocklength.append(blocklen)
            buf = []
        else:
            buf.append(c)
    blocks.append((blocklen, buf))
    taillength.append(len(buf))
    blocklen += len(buf)
    blocklength.append(blocklen)
    blocklen *= 1
    mblocklength.append(blocklen)

    # debug(S, X, msg=":S, X")
    # debug(blocks, msg=":blocks")
    # debug(blocklength, msg=":blocklength")
    # debug(mblocklength, msg=":mblocklength")
    # debug(taillength, msg=":taillength")
    X -= 1

    for i, (bodylen, tail) in enumerate(reversed(blocks)):
        # debug(bodylen, X, tail, msg=":bodylen ,X")
        if X >= bodylen:
            return tail[X - bodylen]
        X %= blocklength[-2 - i]

    return blocks[0][1][X]


def main():
    # parse input
    S = input().strip().decode('ascii')
    X = int(input())
    print(solve(S, X))


# tests
T0 = """
ab1cd
3
"""
TEST_T0 = """
>>> as_input(T0)
>>> main()
a
"""

T01 = """
ab1cd
5
"""
TEST_T01 = """
>>> as_input(T01)
>>> main()
c
"""

T02 = """
abc
1
"""
TEST_T02 = """
>>> as_input(T02)
>>> main()
a
"""

T1 = """
ab2c1
6
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
b
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
