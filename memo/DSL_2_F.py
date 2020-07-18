#!/usr/bin/env python3

# from collections import defaultdict
# from heapq import heappush, heappop
# import numpy as np
import sys

try:
    profile
except:
    def profile(f): return f


def set_depth(depth):
    global DEPTH, SEGTREE_SIZE, NONLEAF_SIZE
    DEPTH = depth
    SEGTREE_SIZE = 1 << DEPTH
    NONLEAF_SIZE = 1 << (DEPTH - 1)


def set_width(width):
    set_depth((width - 1).bit_length() + 1)


@profile
def force_point(value_table, action_table, pos, action_force, action_composite, action_unity):
    action = action_table[pos]
    if action != action_unity:
        value_table[pos] = action

        if pos < NONLEAF_SIZE:
            action_table[pos * 2] = action
            action_table[pos * 2 + 1] = action
    action_table[pos] = action_unity


def down_propagate(table, pos, binop, unity):
    max_level = pos.bit_length() - 1

    for level in range(max_level):
        i = pos >> (max_level - level)
        if table[i] != unity:
            table[i * 2] = table[i]
            table[i * 2 + 1] = table[i]
            table[i] = unity


@profile
def force_range_update(value_table, action_table, left, right, action, action_force, action_composite, action_unity):
    """
    action_force: action, value, cell_size => new_value
    action_composite: new_action, old_action => composite_action
    """
    left += NONLEAF_SIZE
    right += NONLEAF_SIZE
    while left < right:
        if left & 1:
            value_table[left] = action
            if left < NONLEAF_SIZE:
                action_table[left * 2] = action
                action_table[left * 2 + 1] = action
            action_table[left] = action_unity
            left += 1
        if right & 1:
            right -= 1

            value_table[right] = action
            if right < NONLEAF_SIZE:
                action_table[right * 2] = action
                action_table[right * 2 + 1] = action
            action_table[right] = action_unity

        left //= 2
        right //= 2


@profile
def range_reduce(table, left, right, binop, unity):
    ret_left = unity
    ret_right = unity
    left += NONLEAF_SIZE
    right += NONLEAF_SIZE
    while left < right:
        if left & 1:
            ret_left = binop(ret_left, table[left])
            left += 1
        if right & 1:
            right -= 1
            ret_right = binop(table[right], ret_right)

        left //= 2
        right //= 2
    return binop(ret_left, ret_right)


@profile
def up_prop_force(value_table, action_table, pos, binop, action_force, action_composite, action_unity):
    """
    force_children + up_propagation
    """
    while pos > 1:
        pos >>= 1
        force_point(
            value_table, action_table,
            pos * 2, action_force, action_composite, action_unity)

        force_point(
            value_table, action_table,
            pos * 2 + 1, action_force, action_composite, action_unity)
        value_table[pos] = binop(
            value_table[pos * 2],
            value_table[pos * 2 + 1]
        )


@profile
def lazy_range_update(
        action_table, value_table, start, end,
        action, action_composite, action_force, action_unity, value_binop):
    "update [start, end)"
    pos = start + NONLEAF_SIZE
    L = pos // (pos & -pos)
    pos = end + NONLEAF_SIZE
    R = pos // (pos & -pos)

    down_propagate(action_table, L, action_composite, action_unity)
    down_propagate(action_table, R, action_composite, action_unity)
    force_range_update(
        value_table, action_table,
        start, end, action, action_force, action_composite, action_unity)
    up_prop_force(
        value_table, action_table,
        L, value_binop, action_force, action_composite, action_unity)
    up_prop_force(
        value_table, action_table,
        R, value_binop, action_force, action_composite, action_unity)


@profile
def lazy_range_reduce(
    action_table, value_table, start, end,
    action_composite, action_force, action_unity,
    value_binop, value_unity
):
    "reduce [start, end)"
    pos = start + NONLEAF_SIZE
    L = pos // (pos & -pos)
    pos = end + NONLEAF_SIZE
    R = pos // (pos & -pos)

    down_propagate(action_table, L, action_composite, action_unity)
    down_propagate(action_table, R, action_composite, action_unity)
    up_prop_force(
        value_table, action_table,
        L, value_binop, action_force, action_composite, action_unity)
    up_prop_force(
        value_table, action_table,
        R, value_binop,  action_force, action_composite, action_unity)

    return range_reduce(value_table, start, end, value_binop, value_unity)


def main():
    N, Q = map(int, input().split())
    set_width(N)

    value_unity = (1 << 31) - 1
    value_table = [value_unity] * SEGTREE_SIZE
    action_unity = -1
    action_table = [action_unity] * SEGTREE_SIZE

    action_force = None
    action_composite = None

    for _ in range(Q):
        q, *args = map(int, input().split())
        if q == 0:
            # update
            s, t, value = args
            t += 1
            lazy_range_update(
                action_table, value_table, s, t, value,
                action_composite, action_force, action_unity, min)
        else:
            # find
            s, t = args
            print(lazy_range_reduce(
                action_table, value_table, s, t + 1,
                action_composite, action_force, action_unity, min, value_unity))


T1 = """
3 5
0 0 1 1
0 1 2 3
0 2 2 2
1 0 2
1 1 2
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
1
2
"""
T2 = """
1 3
1 0 0
0 0 0 5
1 0 0
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
2147483647
5
"""
T3 = """
8 10
0 1 6 5
0 2 7 2
0 2 5 7
1 3 3
1 2 4
1 0 3
1 5 7
1 2 6
0 3 7 9
1 2 6
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
7
7
5
2
2
7
"""
T4 = """
15 3
0 1 6 5
0 2 7 2
1 6 7
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
2
"""


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


if sys.argv[-1] == "-t":
    print("testing")
    _test()
    sys.exit()

main()
