import sys


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
    max_level = pos.bit_length() - 1
    for level in range(max_level):
        i = pos >> (max_level - level)
        action = table[i]
        if action != -1:
            table[i * 2] = action
            table[i * 2 + 1] = action
            table[i] = -1


def get_size(pos):
    ret = 0
    while pos:
        pos >>= 1
        ret += 1
    return (1 << (N - ret))


def force_point(value_table, action_table, pos, force, composite, unity_action):
    action = action_table[pos]
    #value_table[pos] = force(action, value_table[pos], get_size(pos))
    if action != -1:
        value_table[pos] = action
        if pos < NONLEAF_SIZE:
            action_table[pos * 2] = action
            action_table[pos * 2 + 1] = action
    action_table[pos] = unity_action


def force_children(value_table, action_table, pos, force, composite, unity_action):
    while pos > 1:
        pos >>= 1
        force_point(
            value_table, action_table,
            pos * 2, force, composite, unity_action)
        force_point(
            value_table, action_table,
            pos * 2 + 1, force, composite, unity_action)


def up_prop_force_children(value_table, action_table, pos, binop, force, composite, unity_action):
    """
    force_children + up_propagation
    """
    while pos > 1:
        pos >>= 1
        force_point(
            value_table, action_table,
            pos * 2, force, composite, unity_action)
        force_point(
            value_table, action_table,
            pos * 2 + 1, force, composite, unity_action)
        value_table[pos] = binop(
            value_table[pos * 2],
            value_table[pos * 2 + 1]
        )


def force_range_update(value_table, action_table, value, left, right, force, composite, unity_action):
    """
    force: action, value, cell_size => new_value
    composite: new_action, old_action => composite_action
    """
    left += SEGTREE_SIZE // 2
    right += SEGTREE_SIZE // 2
    while left < right:
        if left & 1:
            action_table[left] = value
            force_point(
                value_table, action_table,
                left, force, composite, unity_action)
            left += 1
        if right & 1:
            right -= 1
            action_table[right] = value
            force_point(
                value_table, action_table,
                right, force, composite, unity_action)
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


def up(pos):
    pos += SEGTREE_SIZE // 2
    return pos // (pos & -pos)


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


def range_reduce(table, left, right, binop, unity):
    ret_left = unity
    ret_right = unity
    left += SEGTREE_SIZE // 2
    right += SEGTREE_SIZE // 2
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
    print(*result, sep="\n", file=sys.stderr)


try:
    profile
except:
    def profile(f): return f


def mainF():
    N, Q = map(int, input().split())

    depth = N.bit_length() + 1
    set_depth(depth)
    value_unity = (1 << 31) - 1
    value_table = [value_unity] * SEGTREE_SIZE
    action_unity = -1
    action_table = [action_unity] * SEGTREE_SIZE

    def force(action, value, size):
        if action == action_unity:
            return value
        return action

    def composite(new_action, old_action):
        if new_action != action_unity:
            return new_action
        return old_action

    for time in range(Q):
        q, *args = map(int, input().split())
        if q == 0:
            # update
            # debug("update: args", args)
            s, t, value = args
            down_propagate(action_table, up(s), composite, action_unity)
            down_propagate(action_table, up(t + 1), composite, action_unity)
            #range_update(action_table, s, t + 1, lambda x: value)
            # debugprint(action_table)

            force_range_update(
                value_table, action_table, value,
                s, t + 1, force, composite, action_unity)
            up_prop_force_children(
                value_table, action_table,
                up(s), min, force, composite, action_unity)
            up_prop_force_children(
                value_table, action_table,
                up(t + 1), min,  force, composite, action_unity)
        else:
            # find
            s, t = args
            down_propagate(action_table, up(s), composite, action_unity)
            down_propagate(action_table, up(t + 1), composite, action_unity)
            up_prop_force_children(
                value_table, action_table,
                up(s), min, force, composite, action_unity)
            up_prop_force_children(
                value_table, action_table,
                up(t + 1), min, force, composite, action_unity)

            # debugprint(action_table)
            # debugprint(value_table)
            print(range_reduce(value_table, s, t + 1, min, value_unity))


T1F = """
3 5
0 0 1 1
0 1 2 3
0 2 2 2
1 0 2
1 1 2
"""
TEST_T1F = """
>>> as_input(T1F)
>>> mainF()
1
2
"""
T2F = """
1 3
1 0 0
0 0 0 5
1 0 0
"""
TEST_T2F = """
>>> as_input(T2F)
>>> mainF()
2147483647
5
"""
T3F = """
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
TEST_T3F = """
>>> as_input(T3F)
>>> mainF()
7
7
5
2
2
7
"""
T4F = """
15 3
0 1 6 5
0 2 7 2
1 6 7
"""
TEST_T4F = """
>>> as_input(T4F)
>>> mainF()
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
