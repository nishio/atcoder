from heapq import *
N = int(input())
T = [None] * N
for i in range(N):
    _, *ts = [int(x) for x in input().split()]
    T[i] = ts
    ts.append(-1)
    ts.append(-1)
M = int(input())
A = [int(x) for x in input().split()]

for1 = []
for2 = []
cursor1 = [0] * N
cursor2 = [1] * N
for i, ts in enumerate(T):
    heappush(for1, (-ts[0], i))
    heappush(for2, (-ts[0], i))
    heappush(for2, (-ts[1], i))

for m in range(M):
    # print(cursor1)
    # print(cursor2)
    # print(for1[:3])
    # print(for2[:3])
    if A[m] == 1:
        while True:
            t, pos = for1[0]
            i1 = cursor1[pos]
            i2 = cursor2[pos]
            if T[pos][i1] == -t:
                # first item
                print(-t)
                heappop(for1)
                T[pos][i1] = None
                cursor1[pos] = i2
                heappush(for1, (-T[pos][i2], pos))
                cursor2[pos] = i2 + 1
                heappush(for2, (-T[pos][i2 + 1], pos))
                break
            heappop(for1)

    else:
        while True:
            t, pos = for2[0]
            i1 = cursor1[pos]
            i2 = cursor2[pos]
            if T[pos][i2] == -t:
                # second item
                print(-t)
                heappop(for2)
                T[pos][i2] = None
                cursor2[pos] = i2 + 1
                heappush(for2, (-T[pos][i2 + 1], pos))
                break
            elif T[pos][i1] == -t:
                # first item
                print(-t)
                heappop(for1)
                heappop(for2)
                T[pos][i1] = None
                cursor1[pos] = i2
                heappush(for1, (-T[pos][i2], pos))
                cursor2[pos] = i2 + 1
                heappush(for2, (-T[pos][i2 + 1], pos))
                break
            heappop(for2)
