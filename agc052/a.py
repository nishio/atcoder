# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, SS):
    INF = 9223372036854775807
    for i in range(3):
        SS[i] = SS[i] * 2
    next0 = [0, 0, 0]
    next1 = [0, 0, 0]

    cursor = [-1, -1, -1]
    def update():
        for i in range(3):
            for pos in range(cursor[i] + 1, 4 * N):
                if SS[i][pos] == 48:
                    next0[i] = pos
                    break
            else:
                next0[i] = INF

            for pos in range(cursor[i] + 1, 4 * N):
                if SS[i][pos] == 49:
                    next1[i] = pos
                    break
            else:
                next1[i] = INF
    update()

    ret = []
    for pos in range(2 * N + 1):
        p0 = max(next0)
        p1 = max(next1)
        if p0 < p1:
            ret.append(48)
            cursor = next0[:]
        else:
            ret.append(49)
            cursor = next1[:]
        update()

    return bytes(ret).decode("ascii")

def main():
    T = int(input())
    for _i in range(T):
        N = int(input())
        S1 = input().strip()
        S2 = input().strip()
        S3 = input().strip()
        debug(_i, msg=":_i")
        print(solve(N, [S1, S2, S3]))

def isSubStr(s, t):
    i = 0
    j = 0
    while i < len(s):
        if s[i] == t[j]:
            i += 1
            j += 1
            if j == len(t):
                return True
        else:
            i += 1
    return False

# tests
T1 = """
2
1
01
01
10
2
0101
0011
1100
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
010
11011
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