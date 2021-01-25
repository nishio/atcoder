# included from snippets/main.py


def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def gen_dot():
    for i in range(9):
        x, y = divmod(i, 3)
        print(
            f"a[{x * 3}] * b[{y}] + "
            f"a[{x * 3 + 1}] * b[{y + 3}] + "
            f"a[{x * 3 + 2}] * b[{y + 6}],")


def dot(a, b):
    return [
        a[0] * b[0] + a[1] * b[3] + a[2] * b[6],
        a[0] * b[1] + a[1] * b[4] + a[2] * b[7],
        a[0] * b[2] + a[1] * b[5] + a[2] * b[8],
        a[3] * b[0] + a[4] * b[3] + a[5] * b[6],
        a[3] * b[1] + a[4] * b[4] + a[5] * b[7],
        a[3] * b[2] + a[4] * b[5] + a[5] * b[8],
        a[6] * b[0] + a[7] * b[3] + a[8] * b[6],
        a[6] * b[1] + a[7] * b[4] + a[8] * b[7],
        a[6] * b[2] + a[7] * b[5] + a[8] * b[8]
    ]


def main():
    N = int(input())
    XY = []
    for _i in range(N):
        XY.append(tuple(map(int, input().split())))
    M = int(input())

    timeline = []
    for i in range(M):
        timeline.append(((i + 1) * 2, tuple(map(int, input().split()))))

    Q = int(input())
    QS = []
    for i in range(Q):
        q = tuple(map(int, input().split()))
        QS.append(q)
        timeline.append((q[0] * 2 + 1, q))
    timeline.sort()

    answer = {}
    trans = [1, 0, 0, 0, 1, 0, 0, 0, 1]

    OP1 = [
        0, -1, 0,
        1, 0, 0,
        0, 0, 1]
    OP2 = [
        0, 1, 0,
        -1, 0, 0,
        0, 0, 1]
    OP3 = [
        -1, 0, 0,
        0, 1, 0,
        0, 0, 1]
    OP4 = [
        1, 0, 0,
        0, -1, 0,
        0, 0, 1]

    for t, x in timeline:
        if t % 2:
            # query
            q = x
            i = q[1] - 1
            x, y = XY[i]
            newXY = dot([x, y, 1, 0, 0, 0, 0, 0, 0], trans)
            answer[q] = (newXY[0], newXY[1])

            # debug(q, answer[q], msg=":q, answer[q]")
        else:
            # ops
            if x[0] == 1:
                trans = dot(trans, OP1)
            elif x[0] == 2:
                trans = dot(trans, OP2)
            elif x[0] == 3:
                P = x[1]
                OP3[6] = 2 * P
                trans = dot(trans, OP3)
            elif x[0] == 4:
                P = x[1]
                OP4[7] = 2 * P
                trans = dot(trans, OP4)

    for q in QS:
        x, y = answer[q]
        print(x, y)


T1 = """
1
1 2
4
1
3 3
2
4 2
5
0 1
1 1
2 1
3 1
4 1
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
1 2
2 -1
4 -1
1 4
1 0
"""

T2 = """
2
1000000000 0
0 1000000000
4
3 -1000000000
4 -1000000000
3 1000000000
4 1000000000
2
4 1
4 2
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
5000000000 4000000000
4000000000 5000000000
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
