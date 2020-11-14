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
    spos.append(-1)
    i = 0
    j = 0
    ret = 0
    while i < len(spos) - 1:
        if spos[i] < tpos[j]:
            # spos_i should be deleted
            next = spos[i + 1]
            if next == -1:
                return -1
            ret += (next - spos[i])
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

T4 = """
1
1
1
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
0
"""

T5 = """
1
0
0
"""
TEST_T5 = """
>>> as_input(T5)
>>> main()
0
"""

T6 = """
1
0
1
"""
TEST_T6 = """
>>> as_input(T6)
>>> main()
-1
"""

T7 = """
6
111111
000000
"""
TEST_T7 = """
>>> as_input(T7)
>>> main()
3
"""


def random_test():
    from random import seed, randint
    for i in range(1000):
        seed(i)
        N = randint(1, 10)
        S = [randint(0, 1) for _i in range(N)]
        T = [randint(0, 1) for _i in range(N)]
        debug(N, S, T, msg=":N,S,T")
        ret = solve(N, S, T)


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
