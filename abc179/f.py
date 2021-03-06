#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def set_depth(depth):
    global N, SEGTREE_SIZE, NONLEAF_SIZE
    N = depth
    SEGTREE_SIZE = 1 << N
    NONLEAF_SIZE = 1 << (N - 1)


def range_update(table, left, right, action):
    left += SEGTREE_SIZE // 2
    right += SEGTREE_SIZE // 2
    while left < right:
        if left & 1:
            table[left] = action(table[left])
            left += 1
        if right & 1:
            right -= 1
            table[right] = action(table[right])
        left //= 2
        right //= 2


def down_propagate_to_leaf(table, pos, binop, unity):
    pos += NONLEAF_SIZE
    down_propagate(table, pos, binop, unity)
    return table[pos]


def down_propagate(table, pos, binop, unity):
    for max_level in range(N):
        if 2 ** max_level > pos:
            max_level -= 1
            break
    for level in range(max_level):
        i = pos >> (max_level - level)

        table[i * 2] = binop(table[i], table[i * 2])
        table[i * 2 + 1] = binop(table[i], table[i * 2 + 1])
        table[i] = unity


def set_items(table, xs):
    for i, x in enumerate(xs, NONLEAF_SIZE):
        table[i] = x


def debugprint(xs, minsize=0, maxsize=None):
    strs = [str(x) for x in xs]
    if maxsize != None:
        for i in range(NONLEAF_SIZE, SEGTREE_SIZE):
            strs[i] = strs[i][:maxsize]
    s = max(len(s) for s in strs[NONLEAF_SIZE:])
    if s > minsize:
        minsize = s

    result = ["|"] * N
    level = 0
    next_level = 2
    for i in range(1, SEGTREE_SIZE):
        if i == next_level:
            level += 1
            next_level *= 2
        width = ((minsize + 1) << (N - 1 - level)) - 1
        result[level] += strs[i].center(width) + "|"
    print(*result, sep="\n")


def solve(SOLVE_PARAMS):
    pass


def main():
    # parse input
    N, Q = map(int, input().split())
    depth = (2 * N).bit_length() + 1
    set_depth(depth)
    action_unity = INF
    table = [action_unity] * SEGTREE_SIZE

    # Dual Segtreeで作りかけ

    def action_force(action, value, size):
        return min(action, value)

    def action_composite(new_action, old_action):
        return min(new_action, old_action)

    def value_binop(a, b):
        return min(a, b)

    for time in range(Q):
        q, x = map(int, input().split())
        if q == 1:
            # find
            down_propagate_to_leaf(table, x, max, action_unity)
            # update

            range_update(table, s, t + 1, lambda x: (time, new_value))
            down_propagate(table, up(5), lambda x, y: x if x else y, 0)
            down_propagate(table, up(15), lambda x, y: x if x else y, 0)

        else:
            # find
            print(down_propagate_to_leaf(
                table, args[0], max, action_unity)[1])


# tests
T1 = """
5 5
1 3
2 3
1 4
2 2
1 2
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
1
"""

T2 = """
200000 0
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
39999200004
"""

T3 = """
176527 15
1 81279
2 22308
2 133061
1 80744
2 44603
1 170938
2 139754
2 15220
1 172794
1 159290
2 156968
1 56426
2 77429
1 97459
2 71282
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
31159505795
"""


def _test():
    import doctest
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
            doctest.run_docstring_examples(g[k], g, name=k)


def as_input(s):
    "use in test, use given string as input file"
    import io
    f = io.StringIO(s.strip())
    g = globals()
    g["input"] = lambda: bytes(f.readline(), "ascii")
    g["read"] = lambda: bytes(f.read(), "ascii")


input = sys.stdin.buffer.readline
read = sys.stdin.buffer.read

if sys.argv[-1] == "-t":
    print("testing")
    _test()
    sys.exit()

main()
