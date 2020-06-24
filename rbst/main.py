"""
RBST numba-able

testdata: ABC170E
"""
from collections import defaultdict
from heapq import heappush, heappop
import sys

# -- RBST
import numpy as np


def main(N, Q, data):
    INF = 10 ** 9 + 1
    SUM_UNITY = 0
    random_state = np.array([123456789, 362436069, 521288629, 88675123])
    values = [SUM_UNITY]
    sizes = [0]  # sizes[0] should 0
    sums = [SUM_UNITY]
    lefts = [0]
    rights = [0]
    ret_left = 0
    ret_right = 0
    root = 0

    def randInt():
        tx, ty, tz, tw = random_state
        tt = tx ^ (tx << 11)
        random_state[0] = ty
        random_state[1] = tz
        random_state[2] = tw
        random_state[3] = tw = (tw ^ (tw >> 19)) ^ (tt ^ (tt >> 8))
        return tw

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

    # k: kindergarden, p: person
    p_to_rate = [0] * (N + 1)  # 1-origin
    p_to_k = [0] * (N + 1)  # 1-origin
    # dsc. order heapq for each k
    MAX_K = 200000
    # k_to_ps = defaultdict(list)
    # k_to_ps = [[] for i in range(MAX_K + 1)]
    k_to_ps = [[(-INF, 0)]]
    for i in range(MAX_K):
        x = [(-INF, 0)]
        k_to_ps.append(x)
        x.pop()
    k_to_ps[0].pop()

    AB = data[:2 * N]
    CD = data[2 * N:]
    AB = AB.reshape(-1, 2)
    CD = CD.reshape(-1, 2)
    for i in range(N):
        #A, B = [int(x) for x in input().split()]
        A, B = AB[i]
        I = i + 1
        p_to_rate[I] = A
        p_to_k[I] = B
        heappush(k_to_ps[B], (-A, I))

    # RBST
    for i in range(MAX_K + 1):
        k = k_to_ps[i]
        if k:
            neg_rate, max_p = k[0]
            insert(-neg_rate)

    answers = [0] * Q
    for t in range(Q):
        #C, D = map(int, input().split())
        C, D = CD[t]
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
    elif len(sys.argv) == 2:
        # input given as file
        input_as_file = open(sys.argv[1])
        input = input_as_file.buffer.readline
        read = input_as_file.buffer.read

    # read parameter
    N, Q = [int(x) for x in input().split()]
    data = np.int64(read().split())
    print(*main(N, Q, data), sep="\n")
