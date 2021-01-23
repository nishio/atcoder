import numpy as np
# included from snippets/main.py


def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    N = int(input())
    XY = []
    for _i in range(N):
        XY.append(tuple(map(int, input().split())))
    M = int(input())
    OPS = []
    for _i in range(M):
        OPS.append(tuple(map(int, input().split())))
    Q = int(input())
    QS = []
    for _q in range(Q):
        QS.append(tuple(map(int, input().split())))

    timeline = []
    for i in range(M):
        timeline.append(((i + 1) * 2, OPS[i]))
    for q in QS:
        timeline.append((q[0] * 2 + 1, q))
    timeline.sort()

    # newX = [1, 0, 0]
    # newY = [0, 1, 0]
    answer = {}
    trans = np.eye(3, dtype=np.int)

    for t, x in timeline:
        if t % 2:
            # query
            q = x
            i = q[1] - 1
            x, y = XY[i]
            newXY = np.array([x, y, 1]).dot(trans)
            # answer[q] = (
            #     newX[0] * x + newX[1] * y,
            #     newY[0] * x + newY[1] * y,
            # )
            answer[q] = (newXY[0], newXY[1])

            # debug(q, answer[q], msg=":q, answer[q]")
        else:
            # ops
            if x[0] == 1:
                trans = trans.dot(np.array([
                    [0, -1, 0],
                    [1, 0, 0],
                    [0, 0, 1]]))

                # def f(p):
                #     (x, y, z) = p
                #     return (-y, x)
            elif x[0] == 2:
                trans = trans.dot(np.array([
                    [0, 1, 0],
                    [-1, 0, 0],
                    [0, 0, 1]]))

                # def f(p):
                #     (x, y) = p
                #     return (y, -x)
            elif x[0] == 3:
                P = x[1]
                trans = trans.dot(
                    np.array([
                        [-1, 0, 2*P],
                        [0, 1, 0],
                        [0, 0, 1]]).T)

                # def f(p):
                #     (x, y) = p
                #     return (P * 2 - x, y)

            elif x[0] == 4:
                P = x[1]
                trans = trans.dot(
                    np.array([
                        [1, 0, 0],
                        [0, -1, 2*P],
                        [0, 0, 1]]).T)

                # def f(p):
                #     (x, y) = p
                #     return (x, P * 2 - y)

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
