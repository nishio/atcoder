#!/usr/bin/env python3
"""
numba-able RBST(Randomized Binary Search Tree)

testdata: AtCoder: ABC170E 
"""
from collections import defaultdict
from heapq import heappush, heappop
import sys
import numpy as np


def dp(*x):  # debugprint
    print(*x)


def main(N, Q, data):
    # --- RBST implementation
    INF = 10 ** 9 + 1
    SUM_UNITY = 0
    random_state = np.array(
        [123456789, 362436069, 521288629, 88675123], dtype=np.int16)

    MAX_NODES = 10 ** 6
    values = np.repeat(SUM_UNITY, MAX_NODES)
    sizes = np.zeros(MAX_NODES, dtype=np.int32)
    sums = np.repeat(SUM_UNITY, MAX_NODES)
    lefts = np.zeros(MAX_NODES, dtype=np.int32)
    rights = np.zeros(MAX_NODES, dtype=np.int32)
    node_id = 1

    ret_left = 0
    ret_right = 0
    roots = np.zeros(2 * 10 ** 5 + 1, dtype=np.int32)

    def randInt():
        tx, ty, tz, tw = random_state
        tt = tx ^ (tx << 11)
        random_state[0] = ty
        random_state[1] = tz
        random_state[2] = tw
        random_state[3] = tw = (tw ^ (tw >> 19)) ^ (tt ^ (tt >> 8))
        return tw

    def create_node(v):
        nonlocal node_id
        i = node_id
        values[i] = v
        sizes[i] = 1
        sums[i] = v
        lefts[i] = 0
        rights[i] = 0
        node_id += 1
        return i

    def update(node):
        sizes[node] = sizes[lefts[node]] + sizes[rights[node]] + 1
        sums[node] = sums[lefts[node]] + sums[rights[node]] + values[node]
        # add extra code here
        return node

    def push(node):
        if not node:
            return
        # add extra code here

    def lower_bound(node, val):
        ret = 0
        while True:
            # dp("lower_bound: node, val", node, val)
            push(node)
            if not node:
                return ret
            if val <= values[node]:
                node = lefts[node]
            else:
                ret += sizes[lefts[node]] + 1
                node = rights[node]

    def upper_bound(node, val):
        ret = 0
        while True:
            push(node)
            if not node:
                return ret
            if val >= values[node]:
                ret += sizes[lefts[node]] + 1
                node = rights[node]
            else:
                node = lefts[node]

    # def get(node, k):
    #     "k: 0-origin"
    #     push(node)
    #     if not node:
    #         return -1
    #     if k == sizes[lefts[node]]:
    #         return values[node]
    #     if k < sizes[lefts[node]]:
    #         return get(lefts[node], k)
    #     return get(rights[node], k - sizes[lefts[node]] - 1)

    def merge(left, right):
        is_left = []
        left_snapshot = []
        right_snapshot = []
        ret = 0
        while True:
            push(left)
            push(right)

            if not left or not right:
                if left:
                    ret = left
                else:
                    ret = right
                break
            if randInt() % (sizes[left] + sizes[right]) < sizes[left]:
                is_left.append(True)
                left_snapshot.append(left)
                right_snapshot.append(right)
                left = rights[left]
            else:
                is_left.append(False)
                left_snapshot.append(left)
                right_snapshot.append(right)
                right = lefts[right]

        for i in range(len(is_left) - 1, -1, -1):
            x = is_left[i]
            left = left_snapshot[i]
            right = right_snapshot[i]
            if x:
                rights[left] = ret
                ret = update(left)
            else:
                lefts[right] = ret
                ret = update(right)
        return ret

    def split(node, k):
        "split tree into [0, k) and [k, n)"
        nonlocal ret_left, ret_right
        is_left = []
        node_snapshot = []
        while True:
            push(node)
            if not node:
                ret_left = 0
                ret_right = 0
                break
            if k <= sizes[lefts[node]]:
                is_left.append(True)
                node_snapshot.append(node)
                node = lefts[node]
                continue
            else:
                is_left.append(False)
                node_snapshot.append(node)
                k -= sizes[lefts[node]] + 1
                node = rights[node]
                continue

        for i in range(len(is_left) - 1, -1, -1):
            x = is_left[i]
            node = node_snapshot[i]
            if x:
                lefts[node] = ret_right
                ret_right = update(node)
            else:
                rights[node] = ret_left
                ret_left = update(node)

    def count(root_id, val):
        return upper_bound(roots[root_id], val) - lower_bound(roots[root_id], val)

    def insert(root_id, val):
        nonlocal ret_left, ret_right
        split(roots[root_id], lower_bound(roots[root_id], val))
        r = merge(ret_left, create_node(val))
        r = merge(r, ret_right)
        roots[root_id] = r

    def erase(root_id, val):
        nonlocal ret_left, ret_right
        # dp("erase: root_id, val", root_id, val)
        if count(root_id, val) == 0:
            return  # erasing absent item
        # print("lowewr_bound", lower_bound(roots[root_id], val))
        split(roots[root_id], lower_bound(roots[root_id], val))
        lhs = ret_left
        # print("lhs: ", node_to_list(lhs))
        split(ret_right, 1)
        rhs = ret_right
        # print("rhs: ", node_to_list(rhs))
        roots[root_id] = merge(lhs, rhs)

    def get_min(root_id):
        cur = roots[root_id]
        while cur:
            minvalue = values[cur]
            cur = lefts[cur]
        return minvalue

    def get_max(root_id):
        cur = roots[root_id]
        while cur:
            maxvalue = values[cur]
            cur = rights[cur]
        return maxvalue

    if 0:  # for debug, pure python mode only
        def node_to_list(node):
            if not node:
                return []
            return (
                node_to_list(lefts[node]) +
                [values[node]] +
                node_to_list(rights[node]))

    # --- end RBST implementation

    # --- ABC170E implementation
    # k: kindergarden, p: person
    p_to_rate = [0] * (N + 1)  # 1-origin
    p_to_k = [0] * (N + 1)  # 1-origin
    # dsc. order heapq for each k
    MAX_K = 200000

    AB = data[:2 * N]
    CD = data[2 * N:]
    AB = AB.reshape(-1, 2)
    CD = CD.reshape(-1, 2)
    for i in range(N):
        A, B = AB[i]
        I = i + 1
        p_to_rate[I] = A
        p_to_k[I] = B
        insert(B, A)

    for i in range(1, MAX_K + 1):
        if roots[i]:
            rate = get_max(i)
            insert(0, rate)

    # for i in range(21):
    #     xs = node_to_list(roots[i])
    #     if len(xs):
    #         print(f"{i}: ", xs)

    answers = [0] * Q
    for t in range(Q):
        C, D = CD[t]
        src = p_to_k[C]
        dst = D
        rateC = p_to_rate[C]
        p_to_k[C] = dst

        # remove from `src`
        # print(f"move {C}(rate:{rateC}) from {src} to {dst}")
        rate = get_max(src)
        if rate == rateC:
            # print("max person leaving")
            erase(0, rate)
            erase(src, rate)
            if roots[src]:
                # find next person
                rate = get_max(src)
                insert(0, rate)
        else:
            # not max person leaving, no update on max_ps
            erase(src, rateC)

        # move to `dst`
        if not roots[dst]:
            # destination is empty
            insert(dst, rateC)
            insert(0, rateC)
        else:
            # compare to existing max person
            rate = get_max(dst)
            if rate < rateC:
                # max person changed
                erase(0, rate)
                insert(0, rateC)
            insert(dst, rateC)

        answers[t] = get_min(0)
        # print(t)
        # for i in range(21):
        #     xs = node_to_list(roots[i])
        #     if len(xs):
        #         print(f"{i}: ", xs)
        # print("answer", answers[t])
    return np.array(answers)


USE_NUMBA = True
if USE_NUMBA and sys.argv[-1] == 'ONLINE_JUDGE' or sys.argv[-1] == '-c':
    print("compiling")
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export('main', 'i8[:](i8,i8,i8[::1])')(main)
    # b1: bool, i4: int32, i8: int64, double: f8, [:], [:, :]
    cc.compile()
    exit()
else:
    input = sys.stdin.buffer.readline
    read = sys.stdin.buffer.read

    if USE_NUMBA and sys.argv[-1] != '-p':
        # -p: pure python mode
        # if not -p, import compiled module
        from my_module import main  # pylint: disable=all
    elif sys.argv[-1] == "-t":
        _test()
        exit()
    elif sys.argv[-1] != '-p' and len(sys.argv) == 2:
        # input given as file
        input_as_file = open(sys.argv[1])
        input = input_as_file.buffer.readline
        read = input_as_file.buffer.read

    # read parameter
    N, Q = [int(x) for x in input().split()]
    data = np.int64(read().split())
    print(*main(N, Q, data), sep="\n")
