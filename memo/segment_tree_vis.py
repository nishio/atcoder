"""
Segment Tree Visualizer

# 1-origin index

>>> debugprint(range(SEGTREE_SIZE))
|                       1                       |
|           2           |           3           |
|     4     |     5     |     6     |     7     |
|  8  |  9  |  10 |  11 |  12 |  13 |  14 |  15 |
|16|17|18|19|20|21|22|23|24|25|26|27|28|29|30|31|

# construction from array

>>> table = [None] * SEGTREE_SIZE
>>> set_items(table, range(16))
>>> full_up(table, lambda x, y: f"{x}+{y}")
>>> debugprint(table, 3)
|             0+1+2+3+4+5+6+7+8+9+10+11+12+13+14+15             |
|        0+1+2+3+4+5+6+7        |     8+9+10+11+12+13+14+15     |
|    0+1+2+3    |    4+5+6+7    |   8+9+10+11   |  12+13+14+15  |
|  0+1  |  2+3  |  4+5  |  6+7  |  8+9  | 10+11 | 12+13 | 14+15 |
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12| 13| 14| 15|


# point update

>>> point_update(table, 3, lambda x: f"f({x})")
>>> debugprint(table, 4)
|                    f(0+1+2+3+4+5+6+7+8+9+10+11+12+13+14+15)                   |
|           f(0+1+2+3+4+5+6+7)          |         8+9+10+11+12+13+14+15         |
|     f(0+1+2+3)    |      4+5+6+7      |     8+9+10+11     |    12+13+14+15    |
|   0+1   |  f(2+3) |   4+5   |   6+7   |   8+9   |  10+11  |  12+13  |  14+15  |
| 0  | 1  | 2  |f(3)| 4  | 5  | 6  | 7  | 8  | 9  | 10 | 11 | 12 | 13 | 14 | 15 |

# range update

>>> table = [""] * SEGTREE_SIZE
>>> set_items(table, range(16))
>>> range_update(table, 1, 11, lambda x: f"f({x})")
>>> debugprint(table, maxsize=4)
|                                                                               |
|                                       |                                       |
|                   |        f()        |                   |                   |
|         |   f()   |         |         |   f()   |         |         |         |
| 0  |f(1)| 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  |f(10| 11 | 12 | 13 | 14 | 15 |

>>> range_update(table, 3, 15, lambda x: f"g({x})")
>>> debugprint(table, maxsize=4)
|                                                                               |
|                                       |                                       |
|                   |       g(f())      |        g()        |                   |
|         |   f()   |         |         |   f()   |         |   g()   |         |
| 0  |f(1)| 2  |g(3)| 4  | 5  | 6  | 7  | 8  | 9  |f(10| 11 | 12 | 13 |g(14| 15 |


# range reduce

>>> set_items(table, range(16))
>>> full_up(table, lambda x, y: f"{x}+{y}")
>>> range_reduce(table, 3, 11, lambda x, y: f"{x}+{y}", unity="0")
'0+3+4+5+6+7+8+9+10+0'

# Bin-op must be associative
>>> range_reduce(table, 3, 11, lambda x, y: f"({x}+{y})", unity="0")
'(((0+3)+4+5+6+7)+(8+9+(10+0)))'

# Point add, range sum

>>> table = [0] * SEGTREE_SIZE
>>> set_items(table, range(16))
>>> full_up(table, lambda x, y: f"{x}+{y}")
>>> debugprint(table)
|     0+1+2+3+4+5+6+7+8+9+10+11+12+13+14+15     |
|    0+1+2+3+4+5+6+7    | 8+9+10+11+12+13+14+15 |
|  0+1+2+3  |  4+5+6+7  | 8+9+10+11 |12+13+14+15|
| 0+1 | 2+3 | 4+5 | 6+7 | 8+9 |10+11|12+13|14+15|
|0 |1 |2 |3 |4 |5 |6 |7 |8 |9 |10|11|12|13|14|15|

>>> point_update(table, 5, lambda x: f"{x}+99")
>>> debugprint(table)
|                    0+1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+99                   |
|           0+1+2+3+4+5+6+7+99          |         8+9+10+11+12+13+14+15         |
|      0+1+2+3      |     4+5+6+7+99    |     8+9+10+11     |    12+13+14+15    |
|   0+1   |   2+3   |  4+5+99 |   6+7   |   8+9   |  10+11  |  12+13  |  14+15  |
| 0  | 1  | 2  | 3  | 4  |5+99| 6  | 7  | 8  | 9  | 10 | 11 | 12 | 13 | 14 | 15 |

>>> range_reduce(table, 3, 11, lambda x, y: f"{x}+{y}", "0")
'0+3+4+5+6+7+99+8+9+10+0'

# Point update, range max

>>> table = [0] * SEGTREE_SIZE
>>> set_items(table, range(16))
>>> full_up(table, max)
>>> debugprint(table)
|                       15                      |
|           7           |           15          |
|     3     |     7     |     11    |     15    |
|  1  |  3  |  5  |  7  |  9  |  11 |  13 |  15 |
|0 |1 |2 |3 |4 |5 |6 |7 |8 |9 |10|11|12|13|14|15|

>>> set_item(table, 5, 99)
>>> debugprint(table)
|                       15                      |
|           7           |           15          |
|     3     |     7     |     11    |     15    |
|  1  |  3  |  5  |  7  |  9  |  11 |  13 |  15 |
|0 |1 |2 |3 |4 |99|6 |7 |8 |9 |10|11|12|13|14|15|

>>> up_propagate_from_leaf(table, 5, max)
>>> debugprint(table)
|                       99                      |
|           99          |           15          |
|     3     |     99    |     11    |     15    |
|  1  |  3  |  99 |  7  |  9  |  11 |  13 |  15 |
|0 |1 |2 |3 |4 |99|6 |7 |8 |9 |10|11|12|13|14|15|

# range add, point get

>>> table = [0] * SEGTREE_SIZE
>>> range_update(table, 1, 11, lambda x: x + 1)
>>> debugprint(table, maxsize=4)
|               0               |
|       0       |       0       |
|   0   |   1   |   0   |   0   |
| 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 |
|0|1|0|0|0|0|0|0|0|0|1|0|0|0|0|0|

>>> range_update(table, 3, 15, lambda x: x + 2)
>>> debugprint(table, maxsize=4)
|               0               |
|       0       |       0       |
|   0   |   3   |   2   |   0   |
| 0 | 1 | 0 | 0 | 1 | 0 | 2 | 0 |
|0|1|0|2|0|0|0|0|0|0|1|0|0|0|2|0|

>>> down_propagate_to_leaf(table, 5, lambda x, y: x + y, 0)
>>> debugprint(table, maxsize=4)
|               0               |
|       0       |       0       |
|   0   |   0   |   2   |   0   |
| 0 | 1 | 0 | 3 | 1 | 0 | 2 | 0 |
|0|1|0|2|3|3|0|0|0|0|1|0|0|0|2|0|

>>> down_propagate_to_leaf(table, 9, lambda x, y: x + y, 0)
>>> debugprint(table, maxsize=4)
|               0               |
|       0       |       0       |
|   0   |   0   |   0   |   0   |
| 0 | 1 | 0 | 3 | 0 | 2 | 2 | 0 |
|0|1|0|2|3|3|0|0|3|3|1|0|0|0|2|0|

# Lazy Propagation

>>> set_depth(4)
>>> value_table = [""] * SEGTREE_SIZE
>>> set_items(value_table, [chr(i + ord("a")) for i in range(8)])
>>> full_up(value_table, lambda x, y: f"{x}{y}")
>>> debugprint(value_table)
|    abcdefgh   |
|  abcd |  efgh |
| ab| cd| ef| gh|
|a|b|c|d|e|f|g|h|

>>> action_table = [PowAction(1)] * SEGTREE_SIZE
>>> range_update(action_table, 0, 6, PowAction(2))
>>> debugprint(action_table)
|           ^1          |
|     ^2    |     ^1    |
|  ^1 |  ^1 |  ^2 |  ^1 |
|^1|^1|^1|^1|^1|^1|^1|^1|

>>> force_range_update(value_table, action_table, 0, 6, PowAction(1))
>>> debugprint(value_table, minsize=3)
|            abcdefgh           |
|    (abcd)^2   |      efgh     |
|   ab  |   cd  | (ef)^2|   gh  |
| a | b | c | d | e | f | g | h |

>>> debugprint(action_table)
|           ^1          |
|     ^1    |     ^1    |
|  ^2 |  ^2 |  ^1 |  ^1 |
|^1|^1|^1|^1|^2|^2|^1|^1|

>>> up_propagate(value_table, up(0), lambda x, y: f"{x}{y}")
>>> up_propagate(value_table, up(6), lambda x, y: f"{x}{y}")
>>> debugprint(value_table, minsize=4)
|            (abcd)^2(ef)^2gh           |
|      (abcd)^2     |      (ef)^2gh     |
|    ab   |    cd   |  (ef)^2 |    gh   |
| a  | b  | c  | d  | e  | f  | g  | h  |

>>> down_propagate(action_table, up(1), lambda x, y: x(y), PowAction(1))
>>> down_propagate(action_table, up(5), lambda x, y: x(y), PowAction(1))
>>> debugprint(action_table)
|           ^1          |
|     ^1    |     ^1    |
|  ^1 |  ^2 |  ^1 |  ^1 |
|^2|^2|^1|^1|^2|^2|^1|^1|

>>> range_update(action_table, 1, 5, PowAction(3))
>>> debugprint(action_table)
|           ^1          |
|     ^1    |     ^1    |
|  ^1 |  ^6 |  ^1 |  ^1 |
|^2|^6|^1|^1|^6|^2|^1|^1|

>>> force_range_update(value_table, action_table, 1, 5, PowAction(1))
>>> debugprint(value_table, minsize=5)
|                (abcd)^2(ef)^2gh               |
|        (abcd)^2       |        (ef)^2gh       |
|     ab    |   (cd)^6  |   (ef)^2  |     gh    |
|  a  |(b)^6|  c  |  d  |(e)^6|  f  |  g  |  h  |

>>> debugprint(action_table)
|           ^1          |
|     ^1    |     ^1    |
|  ^1 |  ^1 |  ^1 |  ^1 |
|^2|^1|^6|^6|^1|^2|^1|^1|

>>> up_propagate(value_table, up(1), lambda x, y: f"{x}{y}")
>>> up_propagate(value_table, up(5), lambda x, y: f"{x}{y}")
>>> debugprint(value_table, minsize=5)
|              a(b)^6(cd)^6(e)^6fgh             |
|      a(b)^6(cd)^6     |        (e)^6fgh       |
|   a(b)^6  |   (cd)^6  |   (e)^6f  |     gh    |
|  a  |(b)^6|  c  |  d  |(e)^6|  f  |  g  |  h  |
INCORRECT RESULT

"""

import sys


def set_depth(depth):
    global N, SEGTREE_SIZE, NONLEAF_SIZE
    N = depth
    SEGTREE_SIZE = 1 << N
    NONLEAF_SIZE = 1 << (N - 1)


set_depth(5)

debug_indent = 0


def debug(*x):
    global debug_indent
    x = list(x)
    indent = 0
    if x[0].startswith("enter") or x[0][0] == ">":
        indent = 1
    if x[0].startswith("leave") or x[0][0] == "<":
        debug_indent -= 1
    x[0] = "  " * debug_indent + x[0]
    print(*x, file=sys.stderr)
    debug_indent += indent


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


def point_update(table, pos, action):
    pos = pos + NONLEAF_SIZE
    table[pos] = action(table[pos])
    while pos > 1:
        pos >>= 1
        table[pos] = action(table[pos])


def set_items(table, xs):
    for i, x in enumerate(xs, NONLEAF_SIZE):
        table[i] = x


def set_item(table, pos, x):
    table[pos + NONLEAF_SIZE] = x


def full_up(table, binop):
    for i in range(NONLEAF_SIZE - 1, 0, -1):
        table[i] = binop(
            table[2 * i],
            table[2 * i + 1])


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


def up_propagate_from_leaf(table, pos, binop):
    pos += NONLEAF_SIZE
    while pos > 1:
        pos >>= 1
        table[pos] = binop(
            table[pos * 2],
            table[pos * 2 + 1]
        )


def down_propagate_to_leaf(table, pos, binop, unity):
    pos += NONLEAF_SIZE
    down_propagate(table, pos, binop, unity)


def up_propagate(table, pos, binop):
    while pos > 1:
        pos >>= 1
        table[pos] = binop(
            table[pos * 2],
            table[pos * 2 + 1]
        )


def down_propagate(table, pos, binop, unity):
    for max_level in range(N):
        if 2 ** max_level > pos:
            max_level -= 1
            break
    for level in range(max_level):
        i = pos >> (max_level - level)
        assert i > 0
        table[i * 2] = binop(table[i * 2], table[i])
        table[i * 2 + 1] = binop(table[i * 2 + 1], table[i])
        table[i] = unity


def force_point(value_table, action_table, pos, unity_action):
    debug("force_point: pos", pos)
    action = action_table[pos]
    value_table[pos] = action.force(value_table[pos])
    action_table[pos] = unity_action
    if pos < NONLEAF_SIZE:
        action_table[pos * 2] = action(action_table[pos * 2])
        action_table[pos * 2 + 1] = action(action_table[pos * 2 + 1])


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


class PowAction:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"^{self.value}"

    def __call__(self, v):
        assert isinstance(v, PowAction)
        return PowAction(v.value * self.value)

    def force(self, v):
        # assert isinstance(v, int)
        # return v + self.value
        assert isinstance(v, str)
        return f"({v}){self}"


def up(pos):
    pos += SEGTREE_SIZE // 2
    return pos // (pos & -pos)


def main():
    pass


def _test():
    import doctest
    doctest.testmod()


if sys.argv[-1] == "-t":
    print("testing")
    _test()
    # sys.exit()

main()
