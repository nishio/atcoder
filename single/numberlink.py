from collections import defaultdict
from collections import Counter

EMPTY = ord(".")
BLOCK = ord("#")
STAR = ord("*")

data = """
....1....
......23.
..4......
15..6.7.5
....8....
.2.......
..8...6..
7.....4..
........3
"""

# sanity check
c = Counter(data)
for k in c:
    if k in ".#\n":
        continue
    assert c[k] == 2

data = data.strip().splitlines()
HEIGHT = len(data)
WIDTH = len(data[0])
assert all(len(line) == WIDTH for line in data)
WIDTH += 2
HEIGHT += 2
# add sentinel
buf = "#" * WIDTH
for line in data:
    buf += f"#{line}#"
buf += "#" * WIDTH

data = [ord(c) for c in buf]


def show2d(data):
    for y in range(HEIGHT):
        print("".join(chr(x) for x in data[WIDTH * y: WIDTH * (y + 1)]))


show2d(data)
"""
###########
#....1....#
#......23.#
#..4......#
#15..6.7.5#
#....8....#
#.2.......#
#..8...6..#
#7.....4..#
#........3#
###########
"""


def draw_box(border, start, W, H, COLOR):
    border[start:start + W] = [COLOR] * W
    border[start:start + WIDTH * H:WIDTH] = [COLOR] * H
    border[start + W - 1:start + WIDTH * H + W - 1:WIDTH] = [COLOR] * H
    start += WIDTH * (H - 1)
    border[start:start + W] = [COLOR] * W


SIZE = len(data)
border = [EMPTY] * SIZE
draw_box(border, WIDTH + 1, WIDTH - 2, HEIGHT - 2, STAR)
draw_box(border, 0, WIDTH, HEIGHT, BLOCK)
print()
show2d(border)
"""
###########
#*********#
#*.......*#
#*.......*#
#*.......*#
#*.......*#
#*.......*#
#*.......*#
#*.......*#
#*********#
###########
"""

termpos = defaultdict(list)
for i, x in enumerate(data):
    if x in [EMPTY, BLOCK]:
        continue
    termpos[x].append(i)
print(termpos)


def debug(*x):
    import sys
    print(*x, file=sys.stderr)


def b2b_dfs(k):
    start, goal = termpos[k]
    debug("goal", goal)
    stack = [start]
    prev = [None] * SIZE
    while stack:
        pos = stack.pop()
        for d in [-1, 1, -WIDTH, WIDTH]:
            next = pos + d
            if next == goal:
                prev[goal] = pos
                return prev
            if prev[next] is not None:
                # visited
                continue
            if border[next] != STAR:
                continue
            if data[next] != EMPTY:
                continue
            prev[next] = pos
            stack.append(next)

    return None


def connect_b2b():
    # find border-to-border pair
    isUpdated = False
    b2bpairs = []
    for k in termpos:
        if all(border[pos] == STAR for pos in termpos[k]):
            b2bpairs.append(k)
    debug("b2bpairs", [chr(x) for x in b2bpairs])

    for k in b2bpairs:
        prev = b2b_dfs(k)
        if prev:
            isUpdated = True
            start, goal = termpos[k]
            path = [goal]
            pos = goal
            while pos != start:
                pos = prev[pos]
                path.append(pos)
            print(k, path)
            for pos in path:
                if data[pos] == EMPTY:
                    data[pos] = k
                for d in [-1, 1, -WIDTH, WIDTH, -1-WIDTH, 1-WIDTH, -1+WIDTH, 1+WIDTH]:
                    next = pos + d
                    if border[next] == EMPTY:
                        border[next] = STAR
    show2d(data)
    show2d(border)
    return isUpdated


while True:
    if not connect_b2b():
        break
