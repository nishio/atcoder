# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, S, T):
    spos = []
    tpos = []
    diff = 0
    for i in range(N):
        if S[i] == 1:
            spos.append(i)
            diff += 1
        if T[i] == 1:
            tpos.append(i)
            diff -= 1

    if diff % 2 == 1:
        return -1
    if diff < 0:
        return -1

    tpos += [N] * N
    i = 0
    j = 0
    ret = 0
    while i < len(spos):
        if spos[i] < tpos[j]:
            # spos_i should be deleted
            ret += (spos[i + 1] - spos[i])
            i += 2
            continue

        ret += (spos[i] - tpos[j])
        i += 1
        j += 1

    return ret


def main():
    # parse input
    N = int(input())
    S = [x - ord('0') for x in input().strip()]
    T = [x - ord('0') for x in input().strip()]
    print(solve(N, S, T))


# tests
T1 = """
3
001
100
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
2
"""

T2 = """
3
001
110
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
-1
"""

T3 = """
5
10111
01010
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
5
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
