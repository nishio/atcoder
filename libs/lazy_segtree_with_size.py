"""
Lazy Segment Tree: value_binop takes right node size
"""


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
        right = pos * 2 + 1
        size = get_size(right)
        table[pos] = binop(
            table[pos * 2],
            table[right],
            size
        )


def full_up(table, binop):
    for pos in range(NONLEAF_SIZE - 1, 0, -1):
        right = pos * 2 + 1
        size = get_size(right)
        table[pos] = binop(
            table[pos * 2],
            table[right],
            size)


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
            action_table[i * 2] = action_composite(
                action, action_table[i * 2])
            action_table[i * 2 + 1] = action_composite(
                action, action_table[i * 2 + 1])
            action_table[i] = action_unity

            value_table[i * 2] = action_force(
                action, value_table[i * 2], size)
            value_table[i * 2 + 1] = action_force(
                action, value_table[i * 2 + 1], size)


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
    right_size = 0
    while left < right:
        if left & 1:
            size = get_size(left)
            ret_left = binop(ret_left, table[left], size)
            left += 1
        if right & 1:
            right -= 1
            ret_right = binop(table[right], ret_right, right_size)
            right_size += get_size(right)
        left //= 2
        right //= 2
    return binop(ret_left, ret_right, right_size)


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


def init_from_values(values, value_binop, value_unity):
    N = len(values)
    set_width(N)

    value_table = [value_unity] * SEGTREE_SIZE
    value_table[NONLEAF_SIZE:NONLEAF_SIZE + len(values)] = values
    full_up(value_table, value_binop)
    return value_table

# --- end of library ---


def debug(*x):
    print(*x, file=sys.stderr)


def main():
    # verified: https://atcoder.jp/contests/abl/submissions/17089082
    MOD = 998244353
    N, Q = map(int, input().split())

    cache11 = {}
    i = 1
    p = 1
    step = 10
    while i <= N:
        cache11[i] = p
        p = (p * step + p) % MOD
        step = (step * step) % MOD
        i *= 2

    cache10 = {0: 1}
    i = 1
    p = 10
    while i <= N:
        cache10[i] = p
        p = (p * 10) % MOD
        i += 1

    def action_force(action, value, size):
        if action == action_unity:
            return value
        # return int(str(action) * size)
        return (cache11[size] * action) % MOD

    def action_composite(new_action, old_action):
        if new_action == action_unity:
            return old_action
        return new_action

    def value_binop(a, b, size):
        # debug("a, b, size", a, b, size)
        # return (a * (10 ** size) + b) % MOD
        return (a * cache10[size] + b) % MOD

    value_unity = 0
    value_table = init_from_values([1] * N, value_binop, value_unity)

    action_unity = None
    action_table = [action_unity] * SEGTREE_SIZE

    ret = lazy_range_reduce(
        action_table, value_table, 0, N, action_composite, action_force, action_unity,
        value_binop, value_unity)

    for _q in range(Q):
        l, r, d = map(int, input().split())
        lazy_range_update(
            action_table, value_table, l - 1, r, d,
            action_composite, action_force, action_unity, value_binop)

        ret = lazy_range_reduce(
            action_table, value_table, 0, N, action_composite, action_force, action_unity,
            value_binop, value_unity)
        print(ret)


# tests
T1 = """
8 5
3 6 2
1 4 7
3 8 3
2 2 2
4 5 1
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
11222211
77772211
77333333
72333333
72311333
"""

T2 = """
200000 1
123 456 7
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
641437905
"""

T3 = """
4 4
1 1 2
1 2 3
1 3 4
1 4 5
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
2111
3311
4441
5555
"""

T4 = """
4 4
4 4 2
3 4 3
2 4 4
1 4 5
1112
1133
1444
5555
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
1112
1133
1444
5555
"""

T5 = """
9 3
1 9 1
1 9 5
1 9 9
"""
TEST_T5 = """
>>> as_input(T5)
>>> main()
111111111
555555555
1755646
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


if __name__ == "__main__":
    import sys
    input = sys.stdin.buffer.readline
    read = sys.stdin.buffer.read
    if sys.argv[-1] == "-t":
        print("testing")
        _test()
        sys.exit()
    main()
