# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(points):
    ret = f(points)
    goal = (ret["rot"], ret["root"][0], ret["root"][1])
    if goal == (0, 0, 0):
        return 0
    if goal in trans[0]:
        return 1
    if goal in t2[0]:
        return 2
    if goal in t3[0]:
        return 3

    x = ret["root"][0]
    y = ret["root"][1]
    rot = ret["rot"]
    while not (x >= 0 and y >= 0):
        x, y = y, -x
        rot = rot + 1

    if x > y:
        pass


def main():
    global trans, t2, t3
    trans = [
        set(move([0, 0, 1, 0, 0, 1])),
        set(move([0, 0, 1, 0, 0, -1])),
        set(move([0, 0, -1, 0, 0, -1])),
        set(move([0, 0, 0, 1, -1, 0]))]

    t2 = [None] * 4
    for i in range(4):
        buf = []
        for rot, dx, dy in trans[i]:
            for rot2, dx2, dy2 in trans[rot]:
                buf.append((rot2, dx + dx2, dy + dy2))
        t2[i] = set(buf)

    t3 = [None] * 4
    for i in range(4):
        buf = []
        for rot, dx, dy in t2[i]:
            for rot2, dx2, dy2 in trans[rot]:
                buf.append((rot2, dx + dx2, dy + dy2))
        t3[i] = set(buf)

    T = int(input())
    for _t in range(T):
        points = list(map(int, input().split()))
        print(solve(points))

    # parse input
    # print(solve(SOLVE_PARAMS))


def f(points=[0, 0, 1, 0, 0, 1]):
    x1, y1, x2, y2, x3, y3 = points
    x = [x1, x2, x3]
    y = [y1, y2, y3]
    from itertools import permutations
    for i, j, k in permutations([0, 1, 2]):
        if x[i] == x[j] and abs(y[i] - y[j]) == 1:
            if y[i] == y[k] and abs(x[i] - x[k]):
                if y[i] < y[j] and x[i] < x[k]:
                    rot = 0
                if y[i] > y[j] and x[i] < x[k]:
                    rot = 1
                if y[i] > y[j] and x[i] > x[k]:
                    rot = 2
                if y[i] < y[j] and x[i] > x[k]:
                    rot = 3
                return {"root": (x[i], y[i]), "rot": rot, "points": points}


# def move(points=[0, 0, 1, 0, 0, 1]):
#     x1, y1, x2, y2, x3, y3 = points
#     x = [x1, x2, x3]
#     y = [y1, y2, y3]
#     from itertools import permutations
#     for i, j, k in permutations([0, 1, 2]):
#         for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#             ret = f([x[j], y[j], x[k], y[k], x[j] + dx, y[j] + dy])
#             if ret:
#                 yield ret

def move(points=[0, 0, 1, 0, 0, 1]):
    x1, y1, x2, y2, x3, y3 = points
    x = [x1, x2, x3]
    y = [y1, y2, y3]
    from itertools import permutations
    for i, j, k in permutations([0, 1, 2]):
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ret = f([x[j], y[j], x[k], y[k], x[j] + dx, y[j] + dy])
            if ret:
                yield (ret["rot"], ret["root"][0], ret["root"][1])

    # tests


"""
[{'root': (0, 0), 'rot': 0, 'points': [1, 0, 0, 1, 0, 0]},
 {'root': (0, 0), 'rot': 0, 'points': [0, 1, 1, 0, 0, 0]},
 {'root': (0, 0), 'rot': 0, 'points': [0, 0, 0, 1, 1, 0]},
 {'root': (0, 0), 'rot': 3, 'points': [0, 0, 0, 1, -1, 0]},
 {'root': (0, 0), 'rot': 0, 'points': [0, 0, 1, 0, 0, 1]},
 {'root': (0, 0), 'rot': 1, 'points': [0, 0, 1, 0, 0, -1]},

 {'root': (1, 0), 'rot': 3, 'points': [1, 0, 0, 0, 1, 1]},
 {'root': (1, 0), 'rot': 2, 'points': [1, 0, 0, 0, 1, -1]}]

 {'root': (0, 1), 'rot': 1, 'points': [0, 1, 0, 0, 1, 1]},
 {'root': (0, 1), 'rot': 2, 'points': [0, 1, 0, 0, -1, 1]},

 {'root': (1, 1), 'rot': 2, 'points': [1, 0, 0, 1, 1, 1]},
 {'root': (1, 1), 'rot': 2, 'points': [0, 1, 1, 0, 1, 1]},



[{'root': (0, 0), 'rot': 1, 'points': [1, 0, 0, -1, 0, 0]},
 {'root': (0, 0), 'rot': 1, 'points': [0, -1, 1, 0, 0, 0]},
 {'root': (0, 0), 'rot': 1, 'points': [0, 0, 0, -1, 1, 0]},
 {'root': (0, 0), 'rot': 2, 'points': [0, 0, 0, -1, -1, 0]},
 {'root': (0, 0), 'rot': 0, 'points': [0, 0, 1, 0, 0, 1]},
 {'root': (0, 0), 'rot': 1, 'points': [0, 0, 1, 0, 0, -1]},

 {'root': (1, -1), 'rot': 3, 'points': [1, 0, 0, -1, 1, -1]},
 {'root': (1, -1), 'rot': 3, 'points': [0, -1, 1, 0, 1, -1]},

 {'root': (0, -1), 'rot': 0, 'points': [0, -1, 0, 0, 1, -1]},
 {'root': (0, -1), 'rot': 3, 'points': [0, -1, 0, 0, -1, -1]},

 {'root': (1, 0), 'rot': 3, 'points': [1, 0, 0, 0, 1, 1]},
 {'root': (1, 0), 'rot': 2, 'points': [1, 0, 0, 0, 1, -1]}]


 {'root': (0, 0), 'rot': 3, 'points': [0, 1, -1, 0, 0, 0]},
 {'root': (0, 0), 'rot': 3, 'points': [-1, 0, 0, 1, 0, 0]},
 {'root': (0, 0), 'rot': 3, 'points': [0, 0, -1, 0, 0, 1]},
 {'root': (0, 0), 'rot': 2, 'points': [0, 0, -1, 0, 0, -1]},
 {'root': (0, 0), 'rot': 0, 'points': [0, 0, 0, 1, 1, 0]},
 {'root': (0, 0), 'rot': 3, 'points': [0, 0, 0, 1, -1, 0]},

 {'root': (-1, 0), 'rot': 0, 'points': [-1, 0, 0, 0, -1, 1]},
 {'root': (-1, 0), 'rot': 1, 'points': [-1, 0, 0, 0, -1, -1]},

 {'root': (0, 1), 'rot': 1, 'points': [0, 1, 0, 0, 1, 1]},
 {'root': (0, 1), 'rot': 2, 'points': [0, 1, 0, 0, -1, 1]}]

 {'root': (-1, 1), 'rot': 1, 'points': [-1, 0, 0, 1, -1, 1]},
 [{'root': (-1, 1), 'rot': 1, 'points': [0, 1, -1, 0, -1, 1]},


 [{'root': (0, 0), 'rot': 2, 'points': [-1, 0, 0, -1, 0, 0]},
 {'root': (0, 0), 'rot': 2, 'points': [0, -1, -1, 0, 0, 0]},
 {'root': (0, 0), 'rot': 1, 'points': [0, 0, 0, -1, 1, 0]},
 {'root': (0, 0), 'rot': 2, 'points': [0, 0, 0, -1, -1, 0]},
 {'root': (0, 0), 'rot': 3, 'points': [0, 0, -1, 0, 0, 1]},
 {'root': (0, 0), 'rot': 2, 'points': [0, 0, -1, 0, 0, -1]},

 {'root': (0, -1), 'rot': 0, 'points': [0, -1, 0, 0, 1, -1]},
 {'root': (0, -1), 'rot': 3, 'points': [0, -1, 0, 0, -1, -1]},

 {'root': (-1, 0), 'rot': 0, 'points': [-1, 0, 0, 0, -1, 1]},
 {'root': (-1, 0), 'rot': 1, 'points': [-1, 0, 0, 0, -1, -1]}]

 {'root': (-1, -1), 'rot': 0, 'points': [-1, 0, 0, -1, -1, -1]},
 {'root': (-1, -1), 'rot': 0, 'points': [0, -1, -1, 0, -1, -1]},

"""

T1 = """
1
3 2 2 2 2 1
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
4
"""

T2 = """
10
0 0 1 0 0 1
1 0 0 1 1 1
2 -1 1 -1 1 0
1 -2 2 -1 1 -1
-1 2 0 2 -1 3
-1 -2 -2 -2 -2 -3
-2 4 -3 3 -2 3
3 1 4 2 4 1
-4 2 -4 3 -3 3
5 4 5 3 4 4
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
0
1
2
3
4
5
6
7
8
9
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
