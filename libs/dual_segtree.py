"""
Dual Segment Tree / Half Lazy Segment Tree
Range action, Point get

When `action_composite` is commutative:
    Dual Segment Tree
        range action: range_update(table, s, t, new_value, action_composite)
        point get: point_get(table, args[0], action_composite, action_unity)
otherwise
    Half Lazy Segment Tree        
        range action: 
            down_propagate(table, up(s), action_composite, action_unity)
            down_propagate(table, up(t), action_composite, action_unity)
            range_update(table, s, t, new_value, action_composite)
        point get:
            print(point_get(table, args[0], action_composite, action_unity))
"""


def set_depth(depth):
    global N, SEGTREE_SIZE, NONLEAF_SIZE
    N = depth
    SEGTREE_SIZE = 1 << N
    NONLEAF_SIZE = 1 << (N - 1)


def range_update(table, left, right, action, action_composite):
    left += SEGTREE_SIZE // 2
    right += SEGTREE_SIZE // 2
    while left < right:
        if left & 1:
            table[left] = action_composite(table[left], action)
            left += 1
        if right & 1:
            right -= 1
            table[right] = action_composite(table[right], action)
        left //= 2
        right //= 2


def down_propagate_to_leaf(table, pos, action_composite, action_unity):
    pos += NONLEAF_SIZE
    down_propagate(table, pos, action_composite, action_unity)
    return table[pos]


def down_propagate(table, pos, action_composite, action_unity):
    for max_level in range(N):
        if 2 ** max_level > pos:
            max_level -= 1
            break
    for level in range(max_level):
        i = pos >> (max_level - level)

        table[i * 2] = action_composite(table[i * 2], table[i])
        table[i * 2 + 1] = action_composite(table[i * 2 + 1], table[i])
        table[i] = action_unity


def set_items(table, xs):
    for i, x in enumerate(xs, NONLEAF_SIZE):
        table[i] = x


def point_get(table, pos, action_composite, action_unity):
    return down_propagate_to_leaf(
        table, pos, action_composite, action_unity)


def up(pos):
    pos += SEGTREE_SIZE // 2
    return pos // (pos & -pos)


def set_width(width):
    set_depth((width - 1).bit_length() + 1)

# --- end of library ---


def main():
    """
    verified: https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_D
    """
    INF = (2 ** 31) - 1
    N, Q = map(int, input().split())
    set_width(N)

    action_unity = (-1, INF)
    table = [action_unity] * SEGTREE_SIZE
    action_composite = max

    for time in range(Q):
        q, *args = map(int, input().split())
        if q == 0:
            # update
            s, t, new_value = args
            range_update(table, s, t + 1, (time, new_value), action_composite)

        else:
            # find
            print(point_get(table, args[0], action_composite, action_unity)[1])


# tests
T1 = """
3 5
0 0 1 1
0 1 2 3
0 2 2 2
1 0
1 1
"""


TEST_T1 = """
>>> as_input(T1)
>>> main()
1
3
"""

T2 = """
1 3
1 0
0 0 0 5
1 0
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
2147483647
5
"""


def main_half():
    # verified: https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_D
    INF = (2 ** 31) - 1
    N, Q = map(int, input().split())
    set_width(N)

    action_unity = None
    table = [action_unity] * SEGTREE_SIZE
    set_items(table, [INF] * N)

    def action_composite(old_action, new_action):
        if new_action != action_unity:
            return new_action
        return old_action

    def action_force(value, action):
        if action != action_unity:
            return action
        return value

    for _q in range(Q):
        q, *args = map(int, input().split())
        if q == 0:
            # update
            s, t, new_value = args
            t += 1
            down_propagate(table, up(s), action_composite, action_unity)
            down_propagate(table, up(t), action_composite, action_unity)
            range_update(table, s, t, new_value, action_composite)

        else:
            # find
            print(point_get(table, args[0], action_composite, action_unity))


TEST_T1_H = """
>>> as_input(T1)
>>> main_half()
1
3
"""

TEST_T2_H = """
>>> as_input(T2)
>>> main_half()
2147483647
5
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
    g = globals()
    f = io.StringIO(s.strip())

    g["input"] = lambda: bytes(f.readline(), "ascii")
    g["read"] = lambda: bytes(f.read(), "ascii")


if __name__ == "__main__":
    import sys
    if sys.argv[-1] == "-t":
        print("testing")
        _test()
        sys.exit()
    main()
