from collections import defaultdict
GAME = """
51...#...#...
9..#.6.#44...
9.#..3#.39#..
9#10#110#11#0
130#800#6001#
#8...#...#...
99#...#...#..
9.9#...#1...#
#1150#110#106
9#..#...#..#.
99#1..#1..#..
3010.#108#10.
9..#...#5....
""".replace(" ", "")
GAME = GAME.strip("\n").split("\n")
N = len(GAME[0])
data = ["#" * (N + 2)] + [f"#{line}#" for line in GAME] + ["#" * (N + 2)]
print(data)


def str_to_candidates(s):
    """
    >>> str_to_candidates("345")[4]
    True
    """
    return {i: str(i) in s for i in range(10)}


def all_digits():
    return {i: True for i in range(10)}


def candidates_to_str(x):
    posi = ""
    nega = ""
    for i in range(10):
        if x[i]:
            posi += str(i)
        else:
            nega += str(i)
    if len(nega) + 1 < len(posi):
        return "-" + nega
    return posi


candidates = defaultdict(all_digits)


def f(x, y, s):
    if (x, y) not in candidates:
        candidates[(x, y)] = str_to_candidates(s)


f(3, 1, "1234567")
f(3, 10, "789")
f(4, 10, "23")
f(5, 6, "89")
f(5, 12, "01")
f(6, 7, "789")
f(6, 10, "45")
f(7, 8, "34")
f(8, 10, "67")
f(9, 6, "89")
f(10, 13, "01")

seqs = {}
# find row and column
for y in range(N + 1):
    for x in range(N + 1):
        if data[y][x] in "0123456789":
            candidates[(x, y)] = {i: i == int(data[y][x]) for i in range(10)}

        if data[y][x] == "#":
            buf = []
            dx = 1
            if data[y][x + 1] != "#":
                candidates[(x + 1, y)][0] = False
            while data[y][x + dx] != "#":

                # v = data[y][x + dx]
                buf.append((x + dx, y))
                dx += 1
            if buf:
                seqs[("x", x + 1, y)] = buf

            buf = []
            dy = 1
            if data[y + 1][x] != "#":
                candidates[(x, y + 1)][0] = False
            while data[y + dy][x] != "#":
                buf.append((x, y + dy))
                dy += 1
            if buf:
                seqs[("y", x, y + 1)] = buf


def seq_to_str(xs):
    return "".join(["(%s)" % candidates_to_str(candidates[x]) for x in xs])


def candidates_to_list(x):
    """
    >>> candidates_to_list(str_to_candidates("345"))
    [3, 4, 5]
    """
    return [i for i in range(10) if x[i]]


def iterate_all_value(seq):
    """
    >>> list(iterate_all_value([str_to_candidates("12"),str_to_candidates("34")]))
    [13, 14, 23, 24]
    """
    from itertools import product
    from functools import reduce
    xs = [[i for i in range(10) if s[i]] for s in seq]
    for x in product(*xs):
        yield reduce(lambda x, y: x * 10 + y, x)


# newCandidate = [set() for i in range(5)]
# for a in iterate_all_value([candidates[k] for k in seqs[('x', 1, 13)]]):
#     for b in iterate_all_value([candidates[k] for k in seqs[('x', 5, 13)]]):
#         s = str(52761 - a - b)
#         for i in range(5):
#             newCandidate[i].add(int(s[i]))

# for a in iterate_all_value([candidates[k] for k in seqs[('x', 7, 12)]]):
#     for b in iterate_all_value([candidates[k] for k in seqs[('x', 11, 12)]]):
#         s = str(30309 - a - b)
#         for i in range(5):
#             newCandidate[i].add(int(s[i]))

# print(newCandidate)


def max_value(seq):
    """
    >>> max_value([str_to_candidates("12"),str_to_candidates("34")])
    24
    """
    from itertools import product
    from functools import reduce
    assert isinstance(seq, list)
    xs = [max(i for i in range(10) if s[i]) for s in seq]
    return reduce(lambda x, y: x * 10 + y, xs)


def min_value(seq):
    """
    >>> min_value([str_to_candidates("12"),str_to_candidates("34")])
    13
    """
    from itertools import product
    from functools import reduce
    xs = [min(i for i in range(10) if s[i]) for s in seq]
    return reduce(lambda x, y: x * 10 + y, xs)


def foo(baseValue, keys):
    x = baseValue
    for k in keys:
        x -= max_value([candidates[k] for k in seqs[k]])
    frm = x
    x = baseValue
    for k in keys:
        x -= min_value([candidates[k] for k in seqs[k]])
    print(f"{frm} .. {x}")


# foo(51999, [('x', 7, 1), ('x', 11, 1)])
# foo(51999, [('x', 1, 1), ('x', 11, 1)])
# foo(51999, [('x', 1, 1), ('x', 7, 1)])

def bar(baseValue, keys):
    print(baseValue)
    for target in keys:

        frm = baseValue + max_value([candidates[k] for k in seqs[target]])
        for k in keys:
            frm -= max_value([candidates[k] for k in seqs[k]])

        to = baseValue + min_value([candidates[k] for k in seqs[target]])
        for k in keys:
            to -= min_value([candidates[k] for k in seqs[k]])
        print(f"{target}: {frm} .. {to}")


# bar(45996, [('x', 1, 2), ('x', 5, 2), ('x', 9, 2)])

rows = [None, 51999, 45996, 944, 140, 6931, 8937,
        972, 2800, 1366, 575, 389, 30309, 52761]
for i in range(1, N + 1):
    buf = []
    bar(rows[i], [k for k in seqs if k[0] == "x" and k[2] == i])
    print()

cols = [None, 70029, 40004, 1124, 5342, 90011,
        6453, 545, 1774, 70638, 5020, 955, 11911, 70467]
for i in range(1, N + 1):
    buf = []
    bar(cols[i], [k for k in seqs if k[0] == "y" and k[1] == i])
    print()


def _test():
    import doctest
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
            doctest.run_docstring_examples(g[k], g)


_test()
