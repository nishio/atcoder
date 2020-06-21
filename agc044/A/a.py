#!/usr/bin/env python3
import heapq
T = int(input())
# T = 1
for t in range(T):
    N, A, B, C, D = [int(x) for x in input().split()]
    # N, A, B, C, D = 29384293847243, 454353412, 332423423, 934923490, 1
    # import pdb
    # pdb.set_trace()
    MIN_COST = min(A, B, C, D)
    headm = {0: 0}
    head = [(0, 0)]
    heapq.heapify(head)

    tailm = {N: 0}
    tail = [(0, N)]
    heapq.heapify(tail)

    answer = 1e+99

    def putHead(p, c):
        global answer
        if p < 0:
            return
        if headm.get(p, 1e+99) > c:
            headm[p] = c
            heapq.heappush(head, (c, p))
            if p in tailm:
                v = c + tailm[p]
                if v < answer:
                    answer = v

    def stepHead():
        global lastHeadCost
        cost, position = heapq.heappop(head)
        lastHeadCost = cost
        if headm[position] > cost:
            return

        putHead(position * 2, cost + A)
        putHead(position * 3, cost + B)
        putHead(position * 5, cost + C)
        putHead(position + 1, cost + D)
        putHead(position - 1, cost + D)

    def putTail(p, c):
        global answer
        if p < 0:
            return
        if tailm.get(p, 1e+99) > c:
            tailm[p] = c
            heapq.heappush(tail, (c, p))
            v = c + headm.get(p, p * D)
            if v < answer:
                answer = v

    def stepTail():
        global lastTailCost
        cost, position = heapq.heappop(tail)
        lastTailCost = cost
        if tailm[position] > cost:
            return
        if position % 2 == 0:
            putTail(position // 2, cost + A)
        else:
            putTail((position+1) // 2, cost + A + D)
            putTail((position-1) // 2, cost + A + D)

        if position % 3 == 0:
            putTail(position // 3, cost + B)
        elif position % 3 == 1:
            putTail((position-1) // 3, cost + B + D)
            putTail((position+2) // 3, cost + B + D * 2)
        else:
            putTail((position+1) // 3, cost + B + D)
            putTail((position-2) // 3, cost + B + D * 2)

        if position % 5 == 0:
            putTail(position // 5, cost + C)
        elif position % 5 == 1:
            putTail((position-1) // 5, cost + C + D)
            putTail((position+4) // 5, cost + C + D * 4)
        elif position % 5 == 2:
            putTail((position-2) // 5, cost + C + D * 2)
            putTail((position+3) // 5, cost + C + D * 3)
        elif position % 5 == 3:
            putTail((position+2) // 5, cost + C + D * 2)
            putTail((position-3) // 5, cost + C + D * 3)
        elif position % 5 == 4:
            putTail((position+1) // 5, cost + C + D)
            putTail((position-4) // 5, cost + C + D * 4)

        # putTail(position + 1, cost + D)
        # putTail(position - 1, cost + D)

    lastHeadCost = lastTailCost = 0
    while True:
        if head[0][0] < tail[0][0] and False:
            # print("head")
            stepHead()
        else:
            # print("tail")
            stepTail()
        # print(lastHeadCost + lastTailCost + MIN_COST)
        if lastHeadCost + lastTailCost + MIN_COST >= answer:
            print(answer)
            break
