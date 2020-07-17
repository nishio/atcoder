import sys


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


def force_point(value_table, action_table, pos, force, composite, unity_action):
    action = action_table[pos]
    value_table[pos] = force(action, value_table[pos], get_size(pos))
    action_table[pos] = unity_action
    if pos < NONLEAF_SIZE:
        action_table[pos * 2] = composite(action, action_table[pos * 2])
        action_table[pos * 2 + 1] = composite(
            action, action_table[pos * 2 + 1])


def up_propagate(table, pos, binop):
    while pos > 1:
        pos >>= 1
        table[pos] = binop(
            table[pos * 2],
            table[pos * 2 + 1]
        )


def down_propagate(table, pos, binop, unity):
    max_level = pos.bit_length() - 1
    for level in range(max_level):
        i = pos >> (max_level - level)
        table[i * 2] = binop(table[i], table[i * 2])
        table[i * 2 + 1] = binop(table[i], table[i * 2 + 1])
        table[i] = unity


def force_children(value_table, action_table, pos, force, composite, unity_action):
    while pos > 1:
        pos >>= 1
        force_point(
            value_table, action_table,
            pos * 2, force, composite, unity_action)
        force_point(
            value_table, action_table,
            pos * 2 + 1, force, composite, unity_action)


def force_range_update(value_table, action_table, left, right, force, composite, unity_action):
    """
    force: action, value, cell_size => new_value
    composite: new_action, old_action => composite_action
    """
    left += SEGTREE_SIZE // 2
    right += SEGTREE_SIZE // 2
    while left < right:
        if left & 1:
            force_point(
                value_table, action_table,
                left, force, composite, unity_action)
            left += 1
        if right & 1:
            right -= 1
            force_point(
                value_table, action_table,
                right, force, composite, unity_action)
        left //= 2
        right //= 2


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


def show_forced(action_table, value_table, N, force, composite, action_unity):
    table = action_table[:]
    ret = [0] * N
    for i in range(N):
        pos = i + NONLEAF_SIZE
        down_propagate(table, pos, composite, action_unity)
        ret[i] = force(table[pos], value_table[pos], 1)

    return ret


def mainF():
    N, Q = map(int, input().split())
    set_width(N)

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

    for _ in range(Q):
        q, *args = map(int, input().split())
        if q == 0:
            # update
            s, t, value = args
            down_propagate(action_table, up(s), composite, action_unity)
            down_propagate(action_table, up(t + 1), composite, action_unity)
            range_update(action_table, s, t + 1, lambda x: value)

            force_range_update(
                value_table, action_table,
                s, t + 1, force, composite, action_unity)
            force_children(
                value_table, action_table,
                up(s), force, composite, action_unity)
            force_children(
                value_table, action_table,
                up(t + 1), force, composite, action_unity)
            up_propagate(value_table, up(s), min)
            up_propagate(value_table, up(t + 1), min)
        else:
            # find
            s, t = args
            down_propagate(action_table, up(s), composite, action_unity)
            down_propagate(action_table, up(t + 1), composite, action_unity)
            force_children(
                value_table, action_table,
                up(s), force, composite, action_unity)
            force_children(
                value_table, action_table,
                up(t + 1), force, composite, action_unity)
            up_propagate(value_table, up(s), min)
            up_propagate(value_table, up(t + 1), min)

            print(range_reduce(value_table, s, t + 1, min, value_unity))


def mainG():
    from operator import add
    # parse input
    N, Q = map(int, input().split())
    set_width(N)

    value_unity = 0
    value_table = [value_unity] * SEGTREE_SIZE
    value_binop = add
    action_unity = 0
    action_table = [action_unity] * SEGTREE_SIZE

    def force(action, value, size):
        return action * size + value

    def composite(new_action, old_action):
        return new_action + old_action

    for _ in range(Q):
        q, *args = map(int, input().split())
        if q == 0:
            # add
            s, t, value = args
            s -= 1
            t -= 1
            down_propagate(action_table, up(s), composite, action_unity)
            down_propagate(action_table, up(t + 1), composite, action_unity)
            range_update(action_table, s, t + 1, lambda x: x + value)

            force_range_update(
                value_table, action_table,
                s, t + 1, force, composite, action_unity)
            force_children(
                value_table, action_table,
                up(s), force, composite, action_unity)
            force_children(
                value_table, action_table,
                up(t + 1), force, composite, action_unity)
            up_propagate(value_table, up(s), value_binop)
            up_propagate(value_table, up(t + 1), value_binop)
        else:
            # getSum
            s, t = args
            s -= 1
            t -= 1
            down_propagate(action_table, up(s), composite, action_unity)
            down_propagate(action_table, up(t + 1), composite, action_unity)
            force_children(
                value_table, action_table,
                up(s), force, composite, action_unity)
            force_children(
                value_table, action_table,
                up(t + 1), force, composite, action_unity)
            up_propagate(value_table, up(s), value_binop)
            up_propagate(value_table, up(t + 1), value_binop)

            print(range_reduce(value_table, s, t + 1, value_binop, value_unity))


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

T1G = """
3 5
0 1 2 1
0 2 3 2
0 3 3 3
1 1 2
1 2 3
"""
TEST_T1G = """
>>> as_input(T1G)
>>> mainG()
4
8
"""
T2G = """
4 3
1 1 4
0 1 4 1
1 1 4
"""
TEST_T2G = """
>>> as_input(T2G)
>>> mainG()
0
4
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
    g = globals()
    f = io.StringIO(s.strip())

    g["input"] = lambda: bytes(f.readline(), "ascii")
    g["read"] = lambda: bytes(f.read(), "ascii")


if sys.argv[-1] == "-t":
    print("testing")
    _test()
    sys.exit()
