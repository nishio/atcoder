#!/usr/bin/env python3

# from collections import defaultdict
# from heapq import heappush, heappop
# import numpy as np
import sys
import doctest
sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def lazy_range_update(value_table, action_table, left, right, binop, action, unity):
    down_propagate(action_table, up(left), lambda x, y: x(y), unity)
    down_propagate(action_table, up(right), lambda x, y: x(y), unity)
    range_update(action_table, left, right, action)
    force_range_update(value_table, action_table, left, right, unity)
    force_sibling(value_table, action_table, up(left), unity)
    force_sibling(value_table, action_table, up(right), unity)
    up_propagate(value_table, up(left), binop)
    up_propagate(value_table, up(right), binop)


def up_propagate_from_leaf(table, pos, binop):
    pos += NONLEAF_SIZE
    up_propagate(table, pos, binop)


def up_propagate(table, pos, binop):
    while pos > 1:
        pos >>= 1
        table[pos] = binop(
            table[pos * 2],
            table[pos * 2 + 1]
        )


def down_propagate_to_leaf(table, pos, binop, unity):
    "binop(parent, child): new value of child"
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


def get_size(pos):
    ret = 0
    while pos:
        pos >>= 1
        ret += 1
    return (1 << (N - ret))


def force_point(value_table, action_table, pos, unity_action):
    action = action_table[pos]
    value_table[pos] = action.force(value_table[pos], get_size(pos))
    action_table[pos] = unity_action
    if pos < NONLEAF_SIZE:
        action_table[pos * 2] = action(action_table[pos * 2])
        action_table[pos * 2 + 1] = action(action_table[pos * 2 + 1])


def force_sibling(value_table, action_table, pos, unity_action):
    force_point(value_table, action_table, pos, unity_action)
    force_point(value_table, action_table, pos ^ 1, unity_action)


def force_range_update(value_table, action_table, left, right, unity_action):
    left += SEGTREE_SIZE // 2
    right += SEGTREE_SIZE // 2
    while left < right:
        if left & 1:
            force_point(value_table, action_table, left, unity_action)
            left += 1
        if right & 1:
            right -= 1
            force_point(value_table, action_table, right, unity_action)
        left //= 2
        right //= 2


def set_depth(depth):
    global N, SEGTREE_SIZE, NONLEAF_SIZE
    N = depth
    SEGTREE_SIZE = 1 << N
    NONLEAF_SIZE = 1 << (N - 1)


def debug(*x):
    print(*x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    # parse input
    from operator import add
    N, Q = map(int, input().split())

    depth = N.bit_length() + 1
    set_depth(depth)
    table = [0] * SEGTREE_SIZE

    for time in range(Q):
        q, *args = map(int, input().split())
        if q == 0:
            # update
            s, t, value = args
            range_update(table, s, t + 1, lambda x: x + value)

        else:
            # find
            print(down_propagate_to_leaf(
                table, args[0], add, 0))

    print(solve(SOLVE_PARAMS))


def _test():
    import doctest
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
            doctest.run_docstring_examples(g[k], g)


def as_input(s):
    "use in test, use given string as input file"
    import io
    global read, input
    f = io.StringIO(s.strip())

    def input():
        return bytes(f.readline(), "ascii")

    def read():
        return bytes(f.read(), "ascii")

# tests
# add tests above


input = sys.stdin.buffer.readline
read = sys.stdin.buffer.read

if sys.argv[-1] == "-t":
    print("testing")
    _test()
    sys.exit()

main()
