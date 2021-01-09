#!/usr/bin/env python3
from heapq import heappush, heappop
import sys
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve_WA(N, AS, BS):
    acount = [0] * (N + 10)
    bcount = [0] * (N + 10)
    for i in range(N):
        acount[AS[i]] += 1
        bcount[BS[i]] += 1

    # overlap = []
    queue = []
    total_count = []
    for i in range(N + 10):
        t = acount[i] + bcount[i]
        total_count.append(t)
        if acount[i] + bcount[i] > N:
            print("No")
            return
        # if acount[i] and bcount[i]:
        #     overlap.append(i)
        if bcount[i]:
            heappush(queue, (-t, i))

    ret = []
    for i in range(N):
        debug("queue", queue)
        while True:
            cx, x = heappop(queue)
            if -cx != total_count[x]:
                heappush(queue, (-total_count[x], x))
            break

        if x == AS[i]:
            # use another number
            # try:
            while True:
                cy, y = heappop(queue)
                if -cy != total_count[y]:
                    heappush(queue, (-total_count[y], y))
                break

            # except:
            #     print("No")  # last 10 min. (24 WA)
            #     return
            b = y
            ret.append(b)
            bcount[b] -= 1
            if bcount[b]:
                heappush(queue, (cy + 1, y))
            heappush(queue, (cx, x))
        else:
            b = x
            ret.append(b)
            bcount[b] -= 1
            if bcount[b]:
                heappush(queue, (cx + 1, x))
        total_count[AS[i]] -= 1
        total_count[b] -= 1

    print("Yes")
    print(*ret, sep=" ")


def solve(N, AS, BS):
    from collections import Counter
    a_count = Counter(AS)
    b_count = Counter(BS)

    max_occur = 0
    when_max = None
    for i in range(N + 10):
        t = a_count[i] + b_count[i]
        if t > N:
            return
        if t > max_occur:
            max_occur = t
            when_max = i

    # debug(max_occur, when_max, msg=":max_occur, when_max")
    ret = []
    del a_count[when_max]
    del b_count[when_max]
    a_keys = list(a_count.keys())
    b_keys = list(b_count.keys())
    a_pointer = 0
    b_pointer = 0
    a_len = len(a_keys)
    b_len = len(b_keys)
    for _i in range(N - max_occur):
        # debug(a_keys, b_keys, msg=":a_keys, b_keys")
        # debug(a_pointer, b_pointer, msg=":a_pointer, b_pointer")
        a = a_keys[a_pointer]
        if a == when_max:
            a_pointer = (a_pointer + 1) % a_len
            a = a_keys[a_pointer]
        c = a_count[a]
        if c == 0:
            del a_count[a]
            a_pointer = (a_pointer + 1) % a_len
            a = a_keys[a_pointer]

        # debug(a, msg=":a")
        b = b_keys[b_pointer]
        while a == b or b == when_max or b_count[b] == 0:
            b_pointer = (b_pointer + 1) % b_len
            b = b_keys[b_pointer]

        ret.append((a, b))
        a_count[a] -= 1
        b_count[b] -= 1

    # debug(a_count, b_count, msg=":a_count, b_count")
    for b in b_count:
        for _i in range(b_count[b]):
            ret.append((when_max, b))
    for a in a_count:
        for _i in range(a_count[a]):
            ret.append((a, when_max))

    # debug(ret, msg=":ret")
    ret.sort()
    ret = [b for a, b in ret]
    return ret


def main():
    # parse input
    N = int(input())
    AS = list(map(int, input().split()))
    BS = list(map(int, input().split()))
    ret = solve(N, AS, BS)
    if ret:
        print("Yes")
        print(*ret, sep=" ")
    else:
        print("No")


# tests
T01 = """
2
1 1
1 1
"""
TEST_T01 = """
>>> as_input(T01)
>>> main()
No
"""

T02 = """
2
1 1
1 2
"""
TEST_T02 = """
>>> as_input(T02)
>>> main()
No
"""

T03 = """
2
1 3
2 3
"""
TEST_T03 = """
>>> as_input(T03)
>>> main()
Yes
3 2
"""

T04 = """
2
1 2
1 3
"""
TEST_T04 = """
>>> as_input(T04)
>>> main()
Yes
3 1
"""

T05 = """
2
1 2
1 2
"""
TEST_T05 = """
>>> as_input(T05)
>>> main()
Yes
2 1
"""

T1 = """
6
1 1 1 2 2 3
1 1 1 2 2 3
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
Yes
2 2 3 1 1 1
"""

T2 = """
5
1 1 2 2 3
1 1 2 2 3
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
Yes
2 2 1 3 1
"""

T3 = """
3
1 2 3
1 2 3
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
Yes
2 3 1
"""

T4 = """
3
1 1 1
2 3 4
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
Yes
2 3 4
"""

T5 = """
3
1 2 3
4 5 6
"""
TEST_T5 = """
>>> as_input(T5)
>>> main()
Yes
6 4 5
"""


def random_test():
    from random import seed, randint
    from collections import Counter
    for s in range(1000):
        seed(s)
        N = 5
        AS = [randint(1, 10) for _i in range(N)]
        BS = [randint(1, 10) for _i in range(N)]
        AS.sort()
        BS.sort()
        ret = solve(N, AS, BS)
        if ret:
            if Counter(BS) != Counter(ret):
                print(s)
                print(AS)
                print(BS, Counter(BS))
                print(ret, Counter(ret))
            if any(AS[i] == ret[i] for i in range(N)):
                print(s)
                print(AS)
                print(BS)
                print(ret)


def _test():
    import doctest
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_T5"):
            doctest.run_docstring_examples(g[k], g, name=k)


def as_input(s):
    "use in test, use given string as input file"
    import io
    f = io.StringIO(s.strip())
    g = globals()
    g["input"] = lambda: bytes(f.readline(), "ascii")
    g["read"] = lambda: bytes(f.read(), "ascii")


input = sys.stdin.buffer.readline
read = sys.stdin.buffer.read

if sys.argv[-1] == "-t":
    print("testing")
    _test()
    sys.exit()

main()
