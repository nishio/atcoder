#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def set_depth(depth):
    global DEPTH, SEGTREE_SIZE, NONLEAF_SIZE
    DEPTH = depth
    SEGTREE_SIZE = 1 << DEPTH
    NONLEAF_SIZE = 1 << (DEPTH - 1)


def set_width(width):
    set_depth((width - 1).bit_length() + 1)


def get_size(pos):
    ret = pos.bit_length()
    return (1 << (DEPTH - ret))


def up(pos):
    pos += SEGTREE_SIZE // 2
    return pos // (pos & -pos)


def up_propagate(table, pos, binop):
    while pos > 1:
        pos >>= 1
        table[pos] = binop(
            table[pos * 2],
            table[pos * 2 + 1]
        )


def force_down_propagate(
    action_table, value_table, pos,
    action_composite, action_force, action_unity
):
    max_level = pos.bit_length() - 1
    size = NONLEAF_SIZE
    for level in range(max_level):
        size //= 2
        i = pos >> (max_level - level)
        action = action_table[i]
        if action != action_unity:
            # action_table[i * 2] = action_composite(
            #     action, action_table[i * 2])
            # action_table[i * 2 + 1] = action_composite(
            #     action, action_table[i * 2 + 1])
            action_table[i * 2] += action
            action_table[i * 2 + 1] += action
            action_table[i] = action_unity
            # value_table[i * 2] = action_force(
            #     action, value_table[i * 2], size)
            # value_table[i * 2 + 1] = action_force(
            #     action, value_table[i * 2 + 1], size)
            value_table[i * 2] += action
            value_table[i * 2 + 1] += action


def force_range_update(
    value_table, action_table, left, right,
    action, action_force, action_composite, action_unity
):
    """
    action_force: action, value, cell_size => new_value
    action_composite: new_action, old_action => composite_action
    """
    left += NONLEAF_SIZE
    right += NONLEAF_SIZE
    while left < right:
        if left & 1:
            value_table[left] = action_force(
                action, value_table[left], get_size(left))
            action_table[left] = action_composite(action, action_table[left])
            left += 1
        if right & 1:
            right -= 1
            value_table[right] = action_force(
                action, value_table[right], get_size(right))
            action_table[right] = action_composite(action, action_table[right])

        left //= 2
        right //= 2


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


def lazy_range_update(
        action_table, value_table, start, end,
        action, action_composite, action_force, action_unity, value_binop):
    "update [start, end)"
    L = up(start)
    R = up(end)
    force_down_propagate(
        action_table, value_table, L,
        action_composite, action_force, action_unity)
    force_down_propagate(
        action_table, value_table, R,
        action_composite, action_force, action_unity)

    # print("action", file=sys.stderr)
    # debugprint(action_table)
    # print("value", file=sys.stderr)
    # debugprint(value_table)
    # print(file=sys.stderr)

    force_range_update(
        value_table, action_table, start, end,
        action, action_force, action_composite, action_unity)
    up_propagate(value_table, L, value_binop)
    up_propagate(value_table, R, value_binop)


def lazy_range_reduce(
    action_table, value_table, start, end,
    action_composite, action_force, action_unity,
    value_binop, value_unity
):
    "reduce [start, end)"
    force_down_propagate(
        action_table, value_table, up(start),
        action_composite, action_force,  action_unity)
    force_down_propagate(
        action_table, value_table, up(end),
        action_composite, action_force, action_unity)

    return range_reduce(value_table, start, end, value_binop, value_unity)


def debugprint(xs, minsize=0, maxsize=None):
    global DEPTH
    strs = [str(x) for x in xs]
    if maxsize != None:
        for i in range(NONLEAF_SIZE, SEGTREE_SIZE):
            strs[i] = strs[i][:maxsize]
    s = max(len(s) for s in strs[NONLEAF_SIZE:])
    if s > minsize:
        minsize = s

    result = ["|"] * DEPTH
    level = 0
    next_level = 2
    for i in range(1, SEGTREE_SIZE):
        if i == next_level:
            level += 1
            next_level *= 2
        width = ((minsize + 1) << (DEPTH - 1 - level)) - 1
        result[level] += strs[i].center(width) + "|"
    print(*result, sep="\n", file=sys.stderr)


def full_up(table, binop):
    for i in range(NONLEAF_SIZE - 1, 0, -1):
        table[i] = binop(
            table[2 * i],
            table[2 * i + 1])


def set_items(table, xs):
    for i, x in enumerate(xs, NONLEAF_SIZE):
        table[i] = x


def main():
    # parse input
    N, Q = map(int, input().split())
    set_width(N)

    value_unity = 10 ** 9
    value_table = [0] * SEGTREE_SIZE
    set_items(value_table, [0] * N)
    full_up(value_table, min)
    value_binop = min
    action_unity = 0
    action_table = [action_unity] * SEGTREE_SIZE

    def force(action, value, size):
        return action + value

    def composite(new_action, old_action):
        return new_action + old_action

    for time in range(Q):
        q, *args = map(int, input().split())
        if q == 0:
            # add
            s, t, value = args
            lazy_range_update(
                action_table, value_table, s, t + 1,
                value, composite, force, action_unity, value_binop)

        else:
            # getSum
            s, t = args
            print(lazy_range_reduce(
                action_table, value_table, s, t + 1,
                composite, force, action_unity, value_binop, value_unity))
        # debugprint(action_table)
        # debugprint(value_table)


# tests
T1 = """
6 7
0 1 3 1
0 2 4 -2
1 0 5
1 0 1
0 3 5 3
1 3 4
1 0 5
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
-2
0
1
-1
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


input = sys.stdin.buffer.readline
read = sys.stdin.buffer.read

if sys.argv[-1] == "-t":
    print("testing")
    _test()
    sys.exit()

main()
