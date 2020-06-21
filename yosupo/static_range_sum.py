from itertools import accumulate
N, Q = map(int, input().split())
AS = list(map(int, input().split()))
AS.append(0)
sums = list(accumulate(AS))
for q in range(Q):
    L, R = map(int, input().split())
    s = sums[R - 1]
    if L > 0:
        s -= sums[L - 1]
    print(s)
