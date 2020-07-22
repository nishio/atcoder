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

>>> point_set(table, 3, "x", lambda x, y: f"{x}+{y}")
>>> debugprint(table, 3)
|             0+1+2+x+4+5+6+7+8+9+10+11+12+13+14+15             |
|        0+1+2+x+4+5+6+7        |     8+9+10+11+12+13+14+15     |
|    0+1+2+x    |    4+5+6+7    |   8+9+10+11   |  12+13+14+15  |
|  0+1  |  2+x  |  4+5  |  6+7  |  8+9  | 10+11 | 12+13 | 14+15 |
| 0 | 1 | 2 | x | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12| 13| 14| 15|

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

# range update

>>> table = [""] * SEGTREE_SIZE
>>> set_items(table, range(16))
>>> range_update(table, 1, 11, lambda x: f"f")
>>> debugprint(table)
|                                               |
|                       |                       |
|           |     f     |           |           |
|     |  f  |     |     |  f  |     |     |     |
|0 |f |2 |3 |4 |5 |6 |7 |8 |9 |f |11|12|13|14|15|

>>> range_update(table, 3, 15, lambda x: f"{x}g")
>>> debugprint(table)
|                                                               |
|                               |                               |
|               |       fg      |       g       |               |
|       |   f   |       |       |   f   |       |   g   |       |
| 0 | f | 2 | 3g| 4 | 5 | 6 | 7 | 8 | 9 | f | 11| 12| 13|14g| 15|


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

# range add, point get (dual segment tree)

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

>>> down_propagate_to_leaf(table, 5, add, 0)
3

>>> debugprint(table, maxsize=4)
|               0               |
|       0       |       0       |
|   0   |   0   |   2   |   0   |
| 0 | 1 | 0 | 3 | 1 | 0 | 2 | 0 |
|0|1|0|2|3|3|0|0|0|0|1|0|0|0|2|0|

>>> down_propagate_to_leaf(table, 9, add, 0)
3

>>> debugprint(table, maxsize=4)
|               0               |
|       0       |       0       |
|   0   |   0   |   0   |   0   |
| 0 | 1 | 0 | 3 | 0 | 2 | 2 | 0 |
|0|1|0|2|3|3|0|0|3|3|1|0|0|0|2|0|

# dual segment tree and down propagation

>>> set_depth(5)
>>> table = [0] * SEGTREE_SIZE
>>> range_update(table, 3, 10, lambda x: "f")
>>> range_update(table, 5, 15, lambda x: "g")
>>> debugprint(table)
|               0               |
|       0       |       0       |
|   0   |   f   |   g   |   0   |
| 0 | 0 | 0 | g | f | 0 | g | 0 |
|0|0|0|f|0|g|0|0|0|0|0|0|0|0|g|0|

>>> table = [0] * SEGTREE_SIZE
>>> range_update(table, 3, 10, lambda x: "f")
>>> down_propagate(table, up(5), lambda x, y: x if x else y, 0)
>>> down_propagate(table, up(15), lambda x, y: x if x else y, 0)
>>> debugprint(table)
|               0               |
|       0       |       0       |
|   0   |   0   |   0   |   0   |
| 0 | 0 | 0 | f | f | 0 | 0 | 0 |
|0|0|0|f|f|f|0|0|0|0|0|0|0|0|0|0|

>>> range_update(table, 5, 15, lambda x: "g")
>>> debugprint(table)
|               0               |
|       0       |       0       |
|   0   |   0   |   g   |   0   |
| 0 | 0 | 0 | g | f | 0 | g | 0 |
|0|0|0|f|f|g|0|0|0|0|0|0|0|0|g|0|

# down propagation targets

>>> table = [0] * SEGTREE_SIZE
>>> down_propagate(table, up(5), lambda x,y: "+", "*")
>>> debugprint(table)
|               *               |
|       *       |       +       |
|   +   |   *   |   0   |   0   |
| 0 | 0 | * | + | 0 | 0 | 0 | 0 |
|0|0|0|0|+|+|0|0|0|0|0|0|0|0|0|0|

# lazy segment tree

>>> set_depth(4)
>>> value_table = [""] * SEGTREE_SIZE
>>> set_items(value_table, [chr(i + ord("a")) for i in range(8)])
>>> full_up(value_table, lambda x, y: f"{x}{y}")
>>> debugprint(value_table)
|    abcdefgh   |
|  abcd |  efgh |
| ab| cd| ef| gh|
|a|b|c|d|e|f|g|h|

>>> action_unity = PowAction(1)
>>> action_table = [action_unity] * SEGTREE_SIZE
>>> debugprint(action_table)
|           ^1          |
|     ^1    |     ^1    |
|  ^1 |  ^1 |  ^1 |  ^1 |
|^1|^1|^1|^1|^1|^1|^1|^1|

>>> L = 0
>>> R = 6
>>> def action_composite(new_action, old_action):
...    return PowAction(new_action.value * old_action.value)

>>> def action_force(action, value):
...     if action.value == 1:
...         new_value = value
...     else:
...         if len(value) > 1:
...             value = f"({value})"
...         new_value = f"{value}{action}"
...     return new_value

>>> combined_table = CombinedTable(action_table, value_table)
>>> range_update(combined_table, L, R, combined_action(PowAction(2), action_composite, action_force))
>>> debugprint(action_table, 3)
|               ^1              |
|       ^2      |       ^1      |
|   ^1  |   ^1  |   ^2  |   ^1  |
| ^1| ^1| ^1| ^1| ^1| ^1| ^1| ^1|
>>> debugprint(value_table, 3)
|            abcdefgh           |
|    (abcd)^2   |      efgh     |
|   ab  |   cd  | (ef)^2|   gh  |
| a | b | c | d | e | f | g | h |

>>> up_propagate(value_table, up(L), lambda x, y: f"{x}{y}")
>>> up_propagate(value_table, up(R), lambda x, y: f"{x}{y}")
>>> debugprint(value_table, 3)
|        (abcd)^2(ef)^2gh       |
|    (abcd)^2   |    (ef)^2gh   |
|   ab  |   cd  | (ef)^2|   gh  |
| a | b | c | d | e | f | g | h |

>>> L = 1
>>> R = 5
>>> down_propagate_force(
...    combined_table, up(L),
...    action_composite, action_force, action_unity)
>>> down_propagate_force(
...    combined_table, up(R),
...    action_composite, action_force, action_unity)

>>> debugprint(action_table)
|           ^1          |
|     ^1    |     ^1    |
|  ^1 |  ^2 |  ^1 |  ^1 |
|^2|^2|^1|^1|^2|^2|^1|^1|

>>> debugprint(value_table)
|        (abcd)^2(ef)^2gh       |
|    (abcd)^2   |    (ef)^2gh   |
| (ab)^2| (cd)^2| (ef)^2|   gh  |
|a^2|b^2| c | d |e^2|f^2| g | h |

>>> range_update(combined_table, L, R, combined_action(
...     PowAction(3), action_composite, action_force))
>>> debugprint(action_table, 3)
|               ^1              |
|       ^1      |       ^1      |
|   ^1  |   ^6  |   ^1  |   ^1  |
| ^2| ^6| ^1| ^1| ^6| ^2| ^1| ^1|

>>> debugprint(value_table, 3)
|                        (abcd)^2(ef)^2gh                       |
|            (abcd)^2           |            (ef)^2gh           |
|     (ab)^2    |   ((cd)^2)^3  |     (ef)^2    |       gh      |
|  a^2  |(b^2)^3|   c   |   d   |(e^2)^3|  f^2  |   g   |   h   |

>>> up_propagate(value_table, up(L), lambda x, y: f"{x}{y}")
>>> up_propagate(value_table, up(R), lambda x, y: f"{x}{y}")
>>> debugprint(value_table, 3)
|                a^2(b^2)^3((cd)^2)^3(e^2)^3f^2gh               |
|      a^2(b^2)^3((cd)^2)^3     |          (e^2)^3f^2gh         |
|   a^2(b^2)^3  |   ((cd)^2)^3  |   (e^2)^3f^2  |       gh      |
|  a^2  |(b^2)^3|   c   |   d   |(e^2)^3|  f^2  |   g   |   h   |

>>> L = 3
>>> R = 5
>>> down_propagate_force(
...     combined_table, up(L),
...     action_composite, action_force, action_unity)
>>> down_propagate_force(
...     combined_table, up(R),
...     action_composite, action_force, action_unity)
>>> value_unity = ""
>>> print(range_reduce(value_table, L, R, lambda x, y: f"{x}{y}", value_unity))
d^6(e^2)^3
"""

import sys
from operator import add


def set_depth(depth):
    global DEPTH, SEGTREE_SIZE, NONLEAF_SIZE
    DEPTH = depth
    SEGTREE_SIZE = 1 << DEPTH
    NONLEAF_SIZE = 1 << (DEPTH - 1)


def set_width(width):
    set_depth((width - 1).bit_length() + 1)


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
    print(*result, sep="\n")


def show_forced(action_table, value_table, N, force, composite, action_unity):
    table = action_table[:]
    ret = [0] * N
    for i in range(N):
        pos = i + NONLEAF_SIZE
        down_propagate(table, pos, composite, action_unity)
        ret[i] = force(table[pos], value_table[pos], 1)

    return ret


def point_update(table, pos, action):
    pos = pos + NONLEAF_SIZE
    table[pos] = action(table[pos])
    while pos > 1:
        pos >>= 1
        table[pos] = action(table[pos])


def point_set(table, pos, value, binop):
    pos = pos + NONLEAF_SIZE
    table[pos] = value
    while pos > 1:
        pos >>= 1
        table[pos] = binop(
            table[pos * 2],
            table[pos * 2 + 1],
        )


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

        table[i * 2] = binop(table[i], table[i * 2])
        table[i * 2 + 1] = binop(table[i], table[i * 2 + 1])
        table[i] = unity


def get_size(pos):
    ret = pos.bit_length()
    return (1 << (DEPTH - ret))


class PowAction:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"^{self.value}"


def up(pos):
    pos += SEGTREE_SIZE // 2
    return pos // (pos & -pos)


class CombinedTable:
    def __init__(self, value, action):
        self.value = value
        self.action = action

    def __getitem__(self, index):
        return (self.value[index], self.action[index])

    def __setitem__(self, index, arg):
        value, action = arg
        self.value[index] = value
        self.action[index] = action


def combined_action(new_action, action_composite, action_force):
    def f(args):
        action, value = args
        return (
            action_composite(new_action, action),
            action_force(new_action, value))
    return f


def down_propagate_force(table, pos, action_composite, action_force, action_unity):
    max_level = pos.bit_length() - 1
    for level in range(max_level):
        i = pos >> (max_level - level)

        action, value = table[i]
        a, v = table[i * 2]
        table[i * 2] = (
            action_composite(action, a),
            action_force(action, v))
        a, v = table[i * 2 + 1]
        table[i * 2 + 1] = (
            action_composite(action, a),
            action_force(action, v))
        table[i] = (action_unity, value)


def _test():
    import doctest
    doctest.testmod()


if sys.argv[-1] == "-t":
    print("testing")
    _test()
    # sys.exit()
