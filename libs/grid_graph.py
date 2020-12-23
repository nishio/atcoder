"""
Construct Grid Graph
"""


def sample(H, W, AS):
    # PAST1J
    from collections import defaultdict
    edges = defaultdict(dict)
    for x in range(W):
        for y in range(H):
            pos = y * W + x
            if x < W - 1:
                edges[pos + 1][pos] = AS[y][x]
            if x > 0:
                edges[pos - 1][pos] = AS[y][x]
            if y < H - 1:
                edges[pos + W][pos] = AS[y][x]
            if y > 0:
                edges[pos - W][pos] = AS[y][x]


def sample2(H, W, data):
    # PAST2H
    from collections import defaultdict
    edges = defaultdict(dict)
    for level in range(10):
        for y in range(H):
            for x in range(W):
                pos = x + y * W + level * W * H
                v = data[y][x]
                if x < W - 1:
                    edges[pos + 1][pos] = 1
                if x > 0:
                    edges[pos - 1][pos] = 1
                if y < H - 1:
                    edges[pos + W][pos] = 1
                if y > 0:
                    edges[pos - W][pos] = 1
                if v == "S":
                    if level == 0:
                        start = pos
                elif v == "G":
                    if level == 9:
                        goal = pos
                else:
                    v = int(v)
                    if v == level:
                        edges[pos - W * H][pos] = 0
