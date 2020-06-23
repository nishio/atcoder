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

    def randInt(t):
        tx, ty, tz, tw = t
        tt = tx ^ (tx << 11)
        t[0] = ty
        t[1] = tz
        t[2] = tw
        t[3] = tw = (tw ^ (tw >> 19)) ^ (tt ^ (tt >> 8))
        return tw

    "Node: val, size, sum, left, right"
    values = [0]
    sizes = [0]
    sums = [0]
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

    def repr(node):
        left = repr(lefts[node]) if lefts[node] else "x"
        right = repr(rights[node]) if rights[node] else "x"
        v = repr(values[self])
        return f"[{left} _{v}_ {right}]"

    def size(node):
        if not node:
            return 0
        return sizes[node]

    def rbst_sum(node):
        if not node:
            return SUM_UNITY
        return sums[node]

    def update(node):
        sizes[node] = size(lefts[node]) + size(rights[node]) + 1
        sums[node] = rbst_sum(lefts[node]) + \
            rbst_sum(rights[node]) + values[node]
        # add extra code here
        return node

    def push(node):
        if not node:
            return
        # add extra code here

    def lower_bound(node, val):
        # dp("lowerbound: node, val", node, val)

        push(node)
        if not node:
            # dp("lowerbound result: 0")
            return 0
        if val <= values[node]:
            # dp("val <= values[node]")
            ret = lower_bound(lefts[node], val)
            # dp("lowerbound result: ret", ret)
            return ret
        # dp("val > values[node]")
        ret = size(lefts[node]) + lower_bound(rights[node], val) + 1
        # dp("lowerbound result: ret", ret)
        return ret

    def upper_bound(node, val):
        push(node)
        if not node:
            return 0
        if val >= values[node]:
            return size(lefts[node]) + upper_bound(rights[node], val) + 1
        return upper_bound(lefts[node], val)

    def get(node, k):
        "k: 0-origin"
        push(node)
        if not node:
            return -1
        if k == size(lefts[node]):
            return values[node]
        if k < size(lefts[node]):
            return get(lefts[node], k)
        return get(rights[node], k - size(lefts[node]) - 1)

    def merge(left, right, t=np.array([123456789, 362436069, 521288629, 88675123])):
        # dp("merge: left,right", left, right)
        push(left)
        push(right)
        if not left or not right:
            if left:
                return left
            return right
        if randInt(t) % (sizes[left] + sizes[right]) < sizes[left]:
            rights[left] = merge(rights[left], right)
            return update(left)
        else:
            lefts[right] = merge(left, lefts[right])
            return update(right)

    def split(node, k):
        "split tree into [0, k) and [k, n)"
        # dp("split: node, k", node, k)
        push(node)
        if not node:
            RBST.ret_left = None
            RBST.ret_right = None
            return
        if k <= size(lefts[node]):
            # dp("split left")
            split(lefts[node], k)
            lefts[node] = RBST.ret_right
            RBST.ret_right = update(node)
            return
        else:
            # dp("split right")
            split(rights[node], k - size(lefts[node]) - 1)
            rights[node] = RBST.ret_left
            RBST.ret_left = update(node)
            return

    class RBST:
        debug = False
        ret_left = None
        ret_right = None

        def __init__(self, node=None):
            self.root = node

        def size(self):
            return size(self.root)

        def sum(self):
            return rbst_sum(self.root)

        def lower_bound(self, val):
            return lower_bound(self.root, val)

        def upper_bound(self, val):
            return upper_bound(self.root, val)

        def count(self, val):
            return self.upper_bound(val) - self.lower_bound(val)

        def get(self, k):
            get(self.root, k)

        def merge(self, add):
            self.root = merge(self.root, add.root)

        def split(self, k):
            split(self.root, k)
            self.root = RBST.ret_left
            return RBST.ret_right

        def insert(self, val):
            split(self.root, self.lower_bound(val))
            r = merge(RBST.ret_left, create_node(val))
            # dp("merge(x1, Node(val)): ", r)
            r = merge(r, RBST.ret_right)
            # dp("merge(r, x2): ", r)
            self.root = r

        def erase(self, val):
            if self.count(val) == 0:
                return
            split(self.root, self.lower_bound(val))
            lhs = RBST.ret_left
            split(RBST.ret_right, 1)
            rhs = RBST.ret_right
            self.root = merge(lhs, rhs)

        def print(self):
            print("{ ", end="")
            print_node(self.root)
            print("}")

        def __repr__(self):
            return repr(node_as_list(self.root))
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
    rbst = RBST()
    for k in k_to_ps:
        neg_rate, max_p = k_to_ps[k][0]
        rbst.insert(-neg_rate)

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
            rbst.erase(-neg_rate)

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
                    rbst.insert(-neg_rate)
                    break
        else:
            # not max person leaving, no update on max_ps
            pass

        # move to `dst`
        if not k_to_ps[dst]:
            # destination is empty
            heappush(k_to_ps[dst], (-rateC, C))
            rbst.insert(rateC)
        else:
            # compare to existing max person
            neg_rate, max_p = k_to_ps[dst][0]
            if -neg_rate < rateC:
                # max person changed
                rbst.erase(-neg_rate)
                rbst.insert(rateC)
            else:
                # no update on max_ps
                pass
            heappush(k_to_ps[dst], (-rateC, C))

        cur = rbst.root
        while cur:
            minvalue = values[cur]
            cur = lefts[cur]
        answers[t] = minvalue
    print(*answers, sep="\n")


def _test():
    import doctest
    doctest.testmod()


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
    main()
