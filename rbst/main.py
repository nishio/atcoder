"""
RBST
ABC170E
"""
from collections import defaultdict
from heapq import heappush, heappop
import sys

# -- RBST
import numpy as np


def main():
    SUM_UNITY = 0

    def randInt():
        tx, ty, tz, tw = random_state
        tt = tx ^ (tx << 11)
        random_state[0] = ty
        random_state[1] = tz
        random_state[2] = tw
        random_state[3] = tw = (tw ^ (tw >> 19)) ^ (tt ^ (tt >> 8))
        return tw

    "Node: val, size, sum, left, right"
    values = [SUM_UNITY]
    sizes = [0]  # sizes[0] should 0
    sums = [SUM_UNITY]
    lefts = [0]
    rights = [0]

    def create_node(v):
        id = len(values)
        values.append(v)
        sizes.append(1)
        sums.append(v)
        lefts.append(0)
        rights.append(0)
        return id

    # not called
    # def repr(node):
    #     left = repr(lefts[node]) if lefts[node] else "x"
    #     right = repr(rights[node]) if rights[node] else "x"
    #     v = repr(values[self])
    #     return f"[{left} _{v}_ {right}]"

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

    # not used
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
        # dp("merge: left,right", left, right)
        push(left)
        push(right)
        if not left or not right:
            if left:
                return left
            return right
        if randInt() % (sizes[left] + sizes[right]) < sizes[left]:
            rights[left] = merge(rights[left], right)
            return update(left)
        else:
            lefts[right] = merge(left, lefts[right])
            return update(right)

    random_state = np.array([123456789, 362436069, 521288629, 88675123])

    def split(node, k):
        nonlocal ret_left, ret_right
        "split tree into [0, k) and [k, n)"
        # dp("split: node, k", node, k)
        push(node)
        if not node:
            ret_left = 0
            ret_right = 0
            return
        if k <= sizes[lefts[node]]:
            # dp("split left")
            split(lefts[node], k)
            lefts[node] = ret_right
            ret_right = update(node)
            return
        else:
            # dp("split right")
            split(rights[node], k - sizes[lefts[node]] - 1)
            rights[node] = ret_left
            ret_left = update(node)
            return

    def count(val):
        return upper_bound(root, val) - lower_bound(root, val)

    def insert(val):
        nonlocal root, ret_left, ret_right
        split(root, lower_bound(root, val))
        r = merge(ret_left, create_node(val))
        # dp("merge(x1, Node(val)): ", r)
        r = merge(r, ret_right)
        # dp("merge(r, x2): ", r)
        root = r

    def erase(val):
        nonlocal root, ret_left, ret_right
        if count(val) == 0:
            return  # erasing absent item
        split(root, lower_bound(root, val))
        lhs = ret_left
        split(ret_right, 1)
        rhs = ret_right
        root = merge(lhs, rhs)

    # classs RBST:
    ret_left = 0
    ret_right = 0
    root = 0

    # class RBST:
    #     debug = False

    # def get(self, k):
    #     get(self.root, k)

    # def merge(self, add):
    #     self.root = merge(self.root, add.root)

    # def split(self, k):
    #     split(self.root, k)
    #     self.root = RBST.ret_left
    #     return RBST.ret_right

    # def print(self):
    #     print("{ ", end="")
    #     print_node(self.root)
    #     print("}")

    # def __repr__(self):
    #     return repr(node_as_list(self.root))
    # -- end RBST

    N, Q = [int(x) for x in input().split()]
    # k: kindergarden, p: person
    p_to_rate = [None] * (N + 1)  # 1-origin
    p_to_k = [None] * (N + 1)  # 1-origin
    # dsc. order heapq for each k
    MAX_K = 200000
    k_to_ps = defaultdict(list)

    for i in range(N):
        A, B = [int(x) for x in input().split()]
        I = i + 1
        p_to_rate[I] = A
        p_to_k[I] = B
        heappush(k_to_ps[B], (-A, I))

    # RBST
    for k in k_to_ps:
        neg_rate, max_p = k_to_ps[k][0]
        insert(-neg_rate)

    answers = [0] * Q
    for t in range(Q):
        C, D = map(int, input().split())
        src = p_to_k[C]
        dst = D
        rateC = p_to_rate[C]
        p_to_k[C] = dst

        # remove from `src`
        # print(f"move {C} from {src} to {dst}")
        neg_rate, max_p = k_to_ps[src][0]
        if max_p == C:
            # print("max person leaving")
            erase(-neg_rate)

            heappop(k_to_ps[src])
            if not k_to_ps[src]:
                # now it is empty
                pass

            else:
                # find next person
                while True:
                    if not k_to_ps[src]:
                        break
                    neg_rate, max_p = k_to_ps[src][0]
                    if p_to_k[max_p] != src:
                        heappop(k_to_ps[src])
                        continue
                    insert(-neg_rate)
                    break
        else:
            # not max person leaving, no update on max_ps
            pass

        # move to `dst`
        if not k_to_ps[dst]:
            # destination is empty
            heappush(k_to_ps[dst], (-rateC, C))
            insert(rateC)
        else:
            # compare to existing max person
            neg_rate, max_p = k_to_ps[dst][0]
            if -neg_rate < rateC:
                # max person changed
                erase(-neg_rate)
                insert(rateC)
            else:
                # no update on max_ps
                pass
            heappush(k_to_ps[dst], (-rateC, C))

        cur = root
        while cur:
            minvalue = values[cur]
            cur = lefts[cur]
        answers[t] = minvalue
    return answers


USE_NUMBA = False
if USE_NUMBA and sys.argv[-1] == 'ONLINE_JUDGE' or sys.argv[-1] == '-c':
    print("compiling")
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export('main', 'void(i8,i8)')(main)
    # b1: bool, i4: int32, i8: int64, double: f8, [:], [:, :]
    cc.compile()
    exit()
else:
    if USE_NUMBA and sys.argv[-1] != '-p':
        # -p: pure python mode
        # if not -p, import compiled module
        from my_module import main  # pylint: disable=all
    elif sys.argv[-1] == "-t":
        _test()
        exit()
    elif len(sys.argv) == 2:
        # input given as file
        input_as_file = open(sys.argv[1])
        input = input_as_file.buffer.readline

    # read parameter
    print(*main(), sep="\n")
