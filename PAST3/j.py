from bisect import bisect_right
N, M = [int(x) for x in input().split()]
XS = [int(x) for x in input().split()]

scores = [0] * N

for x in XS:
    # need to nagate to keep asc. order
    # print("come", x)
    i = bisect_right(scores, -x)
    if i == N:
        print(-1)
    else:
        print(i + 1)
        scores[i] = -x
        # print(scores)
