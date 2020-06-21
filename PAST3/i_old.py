if 0:
    N = int(input())
    Q = int(input())
    queries = []
    for i in range(Q):
        queries.append([int(x) for x in input().split()])
else:
    N = 100000
    queries = [
        [2, 1, 2],
        [4, 1, 2]
    ] * 10000
    queries.append([4, 1, 2])
    Q = len(queries)


def reverseTime(x, y):
    # print(frm)
    for q in reversed(actions):
        f = q[0]
        if f == 3:
            x, y = y, x
        elif f == 1:
            i, j = q[1:]
            if x == i:
                x = j
            elif x == j:
                x = i
        elif f == 2:
            i, j = q[1:]
            if y == i:
                y = j
            elif y == j:
                y = i
    #print(N * (x - 1) + y - 1)


actions = []
for t in range(Q):
    if queries[t][0] == 4:
        _f, i, j = queries[t]
        reverseTime(i, j)
    else:
        actions.append(queries[t])
