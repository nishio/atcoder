#!/usr/bin/env python3
import sys
import heapq

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
# INF = sys.maxsize
INF = 10 ** 9 + 1
# INF = float("inf")


def dp(*x):  # debugprint
    print(*x)


def solve(N, A, B, C, D):
    "void()"

    MIN_COST = min(A, B, C, D)
    headm = {0: 0}
    head = [(0, 0)]
    heapq.heapify(head)

    tailm = {N: 0}
    tail = [(0, N)]
    heapq.heapify(tail)

    answer = 1e+99

    def putHead(p, c):
        nonlocal answer
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
        nonlocal lastHeadCost
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
        nonlocal answer
        if p < 0:
            return
        if tailm.get(p, 1e+99) > c:
            tailm[p] = c
            heapq.heappush(tail, (c, p))
            v = c + headm.get(p, p * D)
            if v < answer:
                answer = v

    def stepTail():
        nonlocal lastTailCost
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
        # print(head, tail)
        if head[0][0] < tail[0][0]:
            # print("head")
            stepHead()
        else:
            # print("tail")
            stepTail()
        # print(head, tail)
        # print(lastHeadCost + lastTailCost + MIN_COST)
        if lastHeadCost + lastTailCost + MIN_COST >= answer:
            print(answer)
            break


def main():
    """
    >>> solve(4, 1000000000, 1000000000, 1000000000, 1)
    4
    """
    T = int(input())
    for t in range(T):
        solve(*[int(x) for x in input().split()])


def _test():
    import doctest
    doctest.testmod()


def as_input(s):
    "use in test, use given string as input file"
    import io
    global read, input
    f = io.StringIO(s.strip())
    input = f.readline
    read = f.read


USE_NUMBA = False
if (USE_NUMBA and sys.argv[-1] == 'ONLINE_JUDGE') or sys.argv[-1] == '-c':
    print("compiling")
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export('solve', solve.__doc__.strip().split()[0])(solve)
    cc.compile()
    exit()
else:
    input = sys.stdin.buffer.readline
    read = sys.stdin.buffer.read

    if (USE_NUMBA and sys.argv[-1] != '-p') or sys.argv[-1] == "--numba":
        # -p: pure python mode
        # if not -p, import compiled module
        from my_module import solve  # pylint: disable=all
    elif sys.argv[-1] == "-t":
        _test()
        sys.exit()
    elif sys.argv[-1] != '-p' and len(sys.argv) == 2:
        # input given as file
        input_as_file = open(sys.argv[1])
        input = input_as_file.buffer.readline
        read = input_as_file.buffer.read

    main()
