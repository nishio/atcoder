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


def force_point(value_table, action_table, pos, action_force, action_composite, action_unity):
    action = action_table[pos]
    # get_size
    size = (1 << (DEPTH - pos.bit_length()))
    # end get_size
    value_table[pos] = action_force(action, value_table[pos], size)
    action_table[pos] = action_unity
    if pos < NONLEAF_SIZE:
        action_table[pos * 2] = action_composite(
            action, action_table[pos * 2])
        action_table[pos * 2 + 1] = action_composite(
            action, action_table[pos * 2 + 1])


def down_propagate(table, pos, binop, unity):
    max_level = pos.bit_length() - 1
    for level in range(max_level):
        i = pos >> (max_level - level)
        table[i * 2] = binop(table[i], table[i * 2])
        table[i * 2 + 1] = binop(table[i], table[i * 2 + 1])
        table[i] = unity


def force_range_update(value_table, action_table, left, right, action, action_force, action_composite, action_unity):
    """
    action_force: action, value, cell_size => new_value
    action_composite: new_action, old_action => composite_action
    """
    left += NONLEAF_SIZE
    right += NONLEAF_SIZE
    while left < right:
        if left & 1:
            action_table[left] = action_composite(action, action_table[left])
            force_point(
                value_table, action_table,
                left, action_force, action_composite, action_unity)
            left += 1
        if right & 1:
            right -= 1
            action_table[right] = action_composite(action, action_table[right])
            force_point(
                value_table, action_table,
                right, action_force, action_composite, action_unity)
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


def show_forced(action_table, value_table, N, action_force, action_composite, action_unity):
    table = action_table[:]
    ret = [0] * N
    for i in range(N):
        pos = i + NONLEAF_SIZE
        down_propagate(table, pos, action_composite, action_unity)
        ret[i] = action_force(table[pos], value_table[pos], 1)

    return ret


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


def mainF():
    N, Q = map(int, input().split())
    set_width(N)

    value_unity = (1 << 31) - 1
    value_table = [value_unity] * SEGTREE_SIZE
    action_unity = -1
    action_table = [action_unity] * SEGTREE_SIZE

    def action_force(action, value, size):
        if action == action_unity:
            return value
        return action

    def action_composite(new_action, old_action):
        if new_action != action_unity:
            return new_action
        return old_action

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

    def action_force(action, value, size):
        return action * size + value

    def action_composite(new_action, old_action):
        return new_action + old_action

    for _ in range(Q):
        q, *args = map(int, input().split())
        if q == 0:
            # add
            s, t, value = args
            s -= 1
            lazy_range_update(
                action_table, value_table, s, t, value,
                action_composite, action_force, action_unity, value_binop)
        else:
            # getSum
            s, t = args
            print(lazy_range_reduce(
                action_table, value_table, s - 1, t,
                action_composite, action_force, action_unity, value_binop, value_unity))


def set_items(table, xs):
    for i, x in enumerate(xs, NONLEAF_SIZE):
        table[i] = x


def mainH():
    # parse input
    N, Q = map(int, input().split())
    set_width(N)

    value_unity = 10 ** 9
    value_table = [value_unity] * SEGTREE_SIZE
    set_items(value_table, [0] * N)
    full_up(value_table, min)

    value_binop = min
    action_unity = 0
    action_table = [action_unity] * SEGTREE_SIZE

    def action_force(action, value, size):
        return action + value

    def action_composite(new_action, old_action):
        return new_action + old_action

    for _ in range(Q):
        q, *args = map(int, input().split())
        if q == 0:
            # add
            s, t, value = args
            t += 1
            lazy_range_update(
                action_table, value_table, s, t, value,
                action_composite, action_force, action_unity, value_binop)
        else:
            # getSum
            s, t = args
            print(lazy_range_reduce(
                action_table, value_table, s, t + 1,
                action_composite, action_force, action_unity, value_binop, value_unity))


def mainI():
    # parse input
    from operator import add
    N, Q = map(int, input().split())
    set_width(N)

    value_unity = 0
    value_table = [0] * SEGTREE_SIZE
    value_binop = add
    action_unity = None
    action_table = [action_unity] * SEGTREE_SIZE

    def action_force(action, value, size):
        if action == action_unity:
            return value
        return action * size

    def action_composite(new_action, old_action):
        if new_action != action_unity:
            return new_action
        return old_action

    for _ in range(Q):
        q, *args = map(int, input().split())
        if q == 0:
            # update
            s, t, value = args
            t += 1
            lazy_range_update(
                action_table, value_table, s, t, value,
                action_composite, action_force, action_unity, value_binop)
        else:
            # getSum
            s, t = args
            print(lazy_range_reduce(
                action_table, value_table, s, t + 1,
                action_composite, action_force, action_unity, value_binop, value_unity))


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

T1H = """
6 7
0 1 3 1
0 2 4 -2
1 0 5
1 0 1
0 3 5 3
1 3 4
1 0 5
"""
TEST_T1H = """
>>> as_input(T1H)
>>> mainH()
-2
0
1
-1
"""

T1I = """
6 7
0 1 3 1
0 2 4 -2
1 0 5
1 0 1
0 3 5 3
1 3 4
1 0 5
"""
TEST_T1I = """
>>> as_input(T1I)
>>> mainI()
-5
1
6
8
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
