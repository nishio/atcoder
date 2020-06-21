N, Q = [int(x) for x in input().split()]

prev = [-table for table in range(N + 1)]
next = [0] * (N + 1)
top = [table for table in range(N + 1)]
bottom = [table for table in range(N + 1)]


def debugPrint():
    blocks = [[] for i in range(N + 1)]
    for table in range(1, N + 1):
        cur = bottom[table]
        while cur:
            blocks[table].append(cur)
            cur = next[cur]

    print(blocks[1:])


for table in range(Q):
    frm, to, x = [int(x) for x in input().split()]
    # print(frm, to, x)

    p = prev[x]
    if p > 0:
        next[p] = 0
        if top[to]:
            prev[x] = top[to]
            next[top[to]] = x
        else:
            # x is first block of TO
            prev[x] = -to
            bottom[to] = x

        top[to] = top[frm]
        top[frm] = p
    else:
        # x is last block
        bottom[frm] = 0
        if top[to]:
            prev[x] = top[to]
            next[top[to]] = x
        else:
            # x is first block of TO
            bottom[to] = x
            top[to] = top[frm]
            prev[x] = -to

        top[to] = top[frm]
        top[frm] = 0

    # print(prev)
    # print(next)
    # print(top)
    # print(bottom)
    # debugPrint()
    # print()


pos = [0] * (N + 1)
for table in range(1, N + 1):
    cur = bottom[table]
    while cur:
        pos[cur] = table
        cur = next[cur]

for i in range(1, N + 1):
    print(pos[i])
