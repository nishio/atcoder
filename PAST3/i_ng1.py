N = int(input())
Q = int(input())
queries = []
for i in range(Q):
    queries.append([int(x) for x in input().split()])


def reverseTime(frm, x, y):

    # print(frm)
    for t in range(frm - 1, -1, -1):
        f, *v = queries[t]
        if f == 4:
            continue
        if f == 3:
            x, y = y, x
        if f == 1:
            i, j = v
            if x == i:
                x = j
            elif x == j:
                x = i
        if f == 2:
            i, j = v
            if y == i:
                y = j
            elif y == j:
                y = i
    print(N * (x - 1) + y - 1)


for t in range(Q):
    if queries[t][0] == 4:
        _f, i, j = queries[t]
        reverseTime(t, i, j)
