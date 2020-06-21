from collections import defaultdict
from heapq import heappush, heappop
N, Q = [int(x) for x in input().split()]
# k: kindergarden, p: person
p_to_rate = [None] * (N + 1)  # 1-origin
p_to_k = [None] * (N + 1)  # 1-origin
# dsc. order heapq for each k
MAX_K = 200000
k_to_ps = [[] for _ in range(MAX_K + 1)]

for i in range(N):
    A, B = [int(x) for x in input().split()]
    I = i + 1
    p_to_rate[I] = A
    p_to_k[I] = B
    heappush(k_to_ps[B], (-A, I))

# asc. order heapq of max score person in each k
max_ps = []
for k in range(MAX_K):
    if k_to_ps[k]:  # k is not empty
        neg_rate, max_p = k_to_ps[k][0]
        heappush(max_ps, (-neg_rate, k, -1))

lastUpdatedOfMax = [-1] * (MAX_K + 1)
# t: time
for t in range(Q):
    C, D = [int(x) for x in input().split()]
    src = p_to_k[C]
    dst = D
    # print("move", src, dst)
    rateC = p_to_rate[C]

    p_to_k[C] = dst
    # remove from `src`
    rate, max_p = k_to_ps[src][0]
    if max_p == C:
        # max person leaving
        # print("max person leaving")
        heappop(k_to_ps[src])
        # find next max person
        while True:
            if not k_to_ps[src]:
                # print("no more person")
                # invalidate old `max` records
                lastUpdatedOfMax[src] = t
                break
            neg_rate, p = k_to_ps[src][0]
            if p == C:
                # duplicated data
                heappop(k_to_ps[src])
                continue
            if p_to_k[p] != src:
                # already moved person
                heappop(k_to_ps[src])
                continue
            # next person found
            heappush(max_ps, (-neg_rate, src, t))
            lastUpdatedOfMax[src] = t
            break
    else:
        # not max person leaving
        # do nothing
        pass

    # move to `dst`
    if not k_to_ps[dst]:
        # destination is empty
        heappush(k_to_ps[dst], (-rateC, C))
        heappush(max_ps, (rateC, dst, t))
        lastUpdatedOfMax[dst] = t
    else:
        # compare to existing max person
        neg_rate, max_p = k_to_ps[dst][0]
        if -neg_rate < rateC:
            # max person updated
            heappush(max_ps, (p_to_rate[C], dst, t))
            lastUpdatedOfMax[dst] = t
        else:
            # do noting
            pass
        heappush(k_to_ps[dst], (-rateC, C))

    # print(list(filter(None, k_to_ps)))
    # print(max_ps)
    while True:
        rate, k, timing = max_ps[0]
        if timing < lastUpdatedOfMax[k]:
            # this record is invalid
            heappop(max_ps)
            continue
        break
    print(rate)
