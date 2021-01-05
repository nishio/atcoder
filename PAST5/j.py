# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve_TLE(S, X):
    blocks = []
    buf = []
    blocklen = 0
    prev_blocklen = 0
    bodylength = []
    blocklength = []
    mblocklength = []
    taillength = []
    bufstart = [0]
    buflen = 0
    for i, c in enumerate(S):
        if c in "123456789":
            c = int(c) + 1
            blocks.append((blocklen, buf))
            taillength.append(buflen)
            blocklen += buflen
            blocklength.append(blocklen)
            blocklen *= c
            mblocklength.append(blocklen)
            bufstart.append(i + 1)
            buflen = 0
            if blocklen > 10 ** 15:
                break
        else:
            buflen += 1
    else:
        blocks.append((blocklen, buf))
        taillength.append(len(buf))
        blocklen += len(buf)
        blocklength.append(blocklen)
        blocklen *= 1
        mblocklength.append(blocklen)

    # debug(S, X, msg="\n:S, X")
    # debug(blocks, msg=":blocks")
    # debug(blocklength, msg=":blocklength")
    # debug(mblocklength, msg=":mblocklength")
    # debug(taillength, msg=":taillength")
    # debug(bufstart, msg=":bufstart")
    # S += "$$$"
    # debug([S[x] for x in bufstart], msg=":bufstart")
    X -= 1

    for i, (bodylen, _) in enumerate(reversed(blocks)):
        # debug(bodylen, X, tail, msg=":bodylen ,X")
        if X >= bodylen:
            start = bufstart[-1-i]
            return S[start + X - bodylen]
        X %= blocklength[-2 - i]

    return blocks[0][1][X]


def solve(S, X):
    X -= 1  # 1-origin to 0-origin
    S += "0"
    blocklen = [0]
    unitlen = [0]
    repeat = [0]
    tailstart = [0]
    taillen = [0]
    tlen = 0
    tstart = 0
    for i, c in enumerate(S):
        if c in "0123456789":
            rep = int(c) + 1
            repeat.append(rep)
            tailstart.append(tstart)
            taillen.append(tlen)
            unitlen.append(blocklen[-1] + tlen)
            blocklen.append(unitlen[-1] * rep)
            if blocklen[-1] > X:
                break
            # next tail
            tstart = i + 1
            tlen = 0
        else:
            tlen += 1

    for i in reversed(range(len(blocklen))):
        X %= unitlen[i]
        if X >= blocklen[i - 1]:
            X -= blocklen[i - 1]
            return S[tailstart[i] + X]


def main():
    # parse input
    S = input().strip().decode('ascii')
    X = int(input())
    print(solve(S, X))


def show_all(S, N):
    print("".join(solve(S, i + 1) for i in range(N)))


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
ab2cd
5
"""
TEST_T02 = """
>>> as_input(T02)
>>> main()
a
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

T2 = """
a1b1
4
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
a
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
