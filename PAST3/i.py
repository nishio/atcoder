if 1:
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


isTransposed = False
xs = list(range(N + 1))
ys = list(range(N + 1))

for q in queries:
    f = q[0]
    if f == 4:
        i, j = q[1:]
        if isTransposed:
            i, j = j, i
        print(N * (xs[i] - 1) + ys[j] - 1)
    elif f == 3:
        isTransposed = not isTransposed
    else:
        i, j = q[1:]
        if (f == 1) ^ isTransposed:
            xs[i], xs[j] = xs[j], xs[i]
        else:
            ys[i], ys[j] = ys[j], ys[i]
