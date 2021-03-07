# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve_WA_TLE(N, SS):
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

def solve(N, SS):
    flag = [1] * 4
    for i in range(3):
        j = (SS[i][0] - 48) + (SS[i][-1] - 48) * 2
        flag[j] = 0

    debug(flag, msg=":flag")
    for i in [0,3,1,2]:
        if flag[i]:
            if i == 0:
                return "0" * N + "1" + "0" * N
            if i == 1:
                return "0" * N + "1" + "1" * N
            if i == 2:
                return "1" * N + "1" + "0" * N
            if i == 3:
                return "1" * N + "0" + "1" * N

def main():
    T = int(input())
    for _i in range(T):
        N = int(input())
        S1 = input().strip()
        S2 = input().strip()
        S3 = input().strip()
        # debug(_i, msg=":_i")
        print(solve(N, [S1, S2, S3][:]))

def maintest():
    T = int(input())
    for _i in range(T):
        N = int(input())
        S1 = input().strip()
        S2 = input().strip()
        S3 = input().strip()
        answer = solve(N, [S1, S2, S3][:])
        print(isOK(N, [S1, S2, S3], bytes(answer, "ascii")))

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

def blute(N, SS):
    import itertools
    for i in range(3):
        SS[i] = (SS[i] * 2).decode("ascii")
    for t in itertools.product("01", repeat=N * 2 + 1):
        if all(isSubStr(s, t) for s in SS):
            print("".join(t))
# blute(2, ["0101", "0011", "1100"])

def isOK(N, SS, answer):
    SS = SS[:]
    for i in range(3):
        SS[i] = SS[i] * 2
    return all(isSubStr(s, answer) for s in SS)

def foo():
    import itertools
    xs = [bytes(x) for x in set(itertools.permutations([48, 48, 49, 49], 4))]
    from random import seed, choice
    N = 2
    for s in range(30):
        seed(s)
        args = [choice(xs), choice(xs), choice(xs)]
        answer = solve(N, args[:])
        if not isOK(N, args[:], bytes(answer, "ascii")):
            ss = [bytes(s).decode("ascii") for s in args]
            print(ss, answer)
            # blute(N, args)
            print()

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
>>> maintest()
True
True
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