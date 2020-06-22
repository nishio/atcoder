#!/usr/bin/env python3
# Randomized Binary Search Tree
# derived from https://qiita.com/drken/items/1b7e6e459c24a83bb7fd


import numpy as np
import time
import numba


def dp(*x):  # debugprint
    if RBST.debug:
        print(*x)


try:
    profile
except:
    def profile(f): return f

SUM_UNITY = 0


@numba.jit("i8(i8[:],i8[:],i8[:],i8[:],i8[:],i8)")
def update(lefts, rights, vals, sizes, sums, node):
    sizes[node] = sizes[lefts[node]] + sizes[rights[node]] + 1
    sums[node] = sums[lefts[node]] + sums[rights[node]] + vals[node]
    # add extra code here
    return node


@numba.jit("void(i8)")
def push(node):
    if not node:
        return
    # add extra code here


def lower_bound(lefts, rights, vals, sizes, node, val):
    ret = 0
    while True:
        # FIXME push(node)
        if not node:
            return ret
        if val <= vals[node]:
            node = lefts[node]
        else:
            ret += sizes[lefts[node]] + 1
            node = rights[node]


def upper_bound(lefts, rights, vals, sizes, sums, node, val):
    push(node)
    if not node:
        return 0
    if val >= vals[node]:
        ret = sizes[lefts[node]]
        ret += upper_bound(
            lefts, rights, vals, sizes, sums,
            rights[node], val) + 1
        return ret
    return upper_bound(lefts, rights, vals, sizes, sums, lefts[node], val)


def get(lefts, rights, vals, sizes, node, k):
    "k: 0-origin"
    push(node)
    if not node:
        return -1
    if k == sizes[lefts[node]]:
        return vals[node]
    if k < sizes[lefts[node]]:
        return get(lefts, rights, vals, sizes, lefts[node], k)
    return get(lefts, rights, vals, sizes,
               rights[node], k - sizes[lefts[node]] - 1)


random_state = np.array([123456789, 362436069, 521288629, 88675123])


def merge(
        lefts, rights, vals, sizes, sums,
        left, right, t):
    is_left = []
    left_snapshot = []
    right_snapshot = []
    ret = 0
    while True:
        # FIXME
        # push(left)
        # push(right)

        if not left or not right:
            if left:
                ret = left
            else:
                ret = right
            break
        if randInt(t) % (sizes[left] + sizes[right]) < sizes[left]:
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
            ret = update(lefts, rights, vals, sizes, sums, left)
        else:
            lefts[right] = ret
            ret = update(lefts, rights, vals, sizes, sums, right)
    return ret


def split(lefts, rights, vals, sizes, sums, ret, node, k):
    "split tree into [0, k) and [k, n)"
    is_left = []
    node_snapshot = []
    while True:
        # FIXME push(node)
        if not node:
            ret[0] = 0
            ret[1] = 0
            break
        if k <= sizes[lefts[node]]:
            is_left.append(True)
            node_snapshot.append(node)
            node = lefts[node]
            continue
        else:
            is_left.append(False)
            node_snapshot.append(node)
            node = rights[node]
            k -= sizes[lefts[node]] + 1
            continue

    for i in range(len(is_left) - 1, -1, -1):
        x = is_left[i]
        node = node_snapshot[i]
        if x:
            lefts[node] = ret[1]
            ret[1] = update(lefts, rights, vals, sizes, sums, node)
        else:
            rights[node] = ret[0]
            ret[0] = update(lefts, rights, vals, sizes, sums, node)


class RBST:
    debug = False

    def __init__(self, node=0):
        self.root = 0
        MAX_NODE_ID = 400_000
        self.vals = np.repeat(SUM_UNITY, MAX_NODE_ID)
        self.sizes = np.ones(MAX_NODE_ID, dtype=np.int)
        self.sums = np.repeat(SUM_UNITY, MAX_NODE_ID)
        self.lefts = np.zeros(MAX_NODE_ID, dtype=np.int)
        self.rights = np.zeros(MAX_NODE_ID, dtype=np.int)
        self.ret = np.zeros(2, dtype=np.int)
        self.sizes[0] = 0
        self.sums[0] = SUM_UNITY
        self.last_id = 0

    def new_node(self, val):
        self.last_id += 1
        self.vals[self.last_id] = val
        self.sums[self.last_id] = val
        return self.last_id

    def lower_bound(self, val):
        return lower_bound(
            self.lefts, self.rights, self.vals, self.sizes,
            self.root, val)

    def upper_bound(self, val):
        return upper_bound(
            self.lefts, self.rights, self.vals, self.sizes, self.sums,
            self.root, val)

    def count(self, val):
        return self.upper_bound(val) - self.lower_bound(val)

    def get(self, k):
        get(
            self.lefts, self.rights, self.vals, self.sizes, self.sums,
            self.root, k)

    def merge(self, add):
        self.root = merge(
            self.lefts, self.rights, self.vals, self.sizes, self.sums,
            self.root, add.root, random_state)

    def split(self, k):
        split(
            self.lefts, self.rights, self.vals, self.sizes, self.sums, self.ret,

            self.root, k)
        self.root = self.ret[0]
        return self.ret[1]

    def insert(self, val):
        split(
            self.lefts, self.rights, self.vals, self.sizes, self.sums, self.ret,
            self.root, self.lower_bound(val))
        r = merge(
            self.lefts, self.rights, self.vals, self.sizes, self.sums,
            self.ret[0], self.new_node(val), random_state)
        # dp("merge(x1, Node(val)): ", r)
        r = merge(
            self.lefts, self.rights, self.vals, self.sizes, self.sums,
            r, self.ret[1], random_state)
        # dp("merge(r, x2): ", r)
        self.root = r

    def erase(self, val):
        if self.count(val) == 0:
            return
        split(
            self.lefts, self.rights, self.vals, self.sizes, self.sums, self.ret,
            self.root, self.lower_bound(val))
        lhs = self.ret[0]
        split(
            self.lefts, self.rights, self.vals, self.sizes, self.sums, self.ret,

            self.ret[1], 1)
        rhs = self.ret[1]
        self.root = merge(
            self.lefts, self.rights, self.vals, self.sizes, self.sums,
            lhs, rhs, random_state)

    def print(self):
        print("{ ", end="")
        self.print_node(self.root)
        print("}")

    def __repr__(self):
        return repr(self.node_as_list(self.root))

    def repr_node(self, node_id):
        left = (self.repr_node(
            self.lefts[node_id])
            if self.lefts[node_id] else "x")
        right = (self.repr_node(
            self.rights[node_id])
            if self.rights[node_id] else "x")
        v = repr(self.vals[node_id])
        return f"[{left} _{v}_ {right}]"

    def node_as_list(self, node):
        if not node:
            return []
        s = [self.vals[node]]
        if self.lefts[node]:
            s = self.node_as_list(self.lefts[node]) + s
        if self.rights[node]:
            s = s + self.node_as_list(self.rights[node])
        return s

    def print_node(self, node):
        if not node:
            return
        self.print_node(self.lefts[node])
        print(self.vals[node], end=" ")
        self.print_node(self.rights[node])

    def print_node_as_tree(self, node, indent=0):
        if not node:
            print(" " * indent + "x")
            return
            # return
        self.print_node_as_tree(self.rights[node], indent + 1)
        print(" " * indent + str(self.vals[node]))
        self.print_node_as_tree(self.lefts[node], indent + 1)


def main():
    """
    >>> r = RBST()
    >>> r
    []
    >>> r.insert(2)
    >>> r
    [2]
    >>> r.print_node_as_tree(r.root)
     x
    2
     x
    >>> r.insert(1)
    >>> r
    [1, 2]
    >>> r.insert(3)
    >>> r
    [1, 2, 3]
    >>> r.erase(2)
    >>> r
    [1, 3]
    """


def _test_count():
    """
    >>> r = RBST()
    >>> RBST.debug = False
    >>> r.insert(1)
    >>> r.print()
    { 1 }
    >>> r.insert(1)
    >>> r.print()
    { 1 1 }
    >>> r.count(1)
    2
    >>> r.insert(1)
    >>> r.print()
    { 1 1 1 }
    >>> r.count(1)
    3
    >>> r = RBST()
    >>> for i in range(100):
    ...     r.insert(1)
    >>> r.count(1)
    100
    """


def _test():
    import doctest
    doctest.testmod()


@numba.jit("i8(i8[:])")
def randInt(t):
    tx, ty, tz, tw = t
    tt = tx ^ (tx << 11)
    t[0] = ty
    t[1] = tz
    t[2] = tw
    t[3] = tw = (tw ^ (tw >> 19)) ^ (tt ^ (tt >> 8))
    return tw


if __name__ == "__main__":
    import sys
    if sys.argv[-1] == "-c":
        # numba compile
        print("compiling")
        from numba.pycc import CC
        cc = CC('numba_rbst')
        cc.export('randInt', 'i8(i8[:])')(randInt)
        cc.export(
            "lower_bound",
            "i8(i8[:],i8[:],i8[:],i8[:],i8,i8)")(
            lower_bound)
        cc.export(
            "update",
            "i8(i8[:],i8[:],i8[:],i8[:],i8[:],i8)")(
            update)
        cc.export(
            "split",
            "void(i8[:],i8[:],i8[:],i8[:],i8[:],i8[:],i8,i8)")(
            split)
        cc.export(
            "merge",
            "i8(i8[:],i8[:],i8[:],i8[:],i8[:],i8,i8,i8[:])")(
            merge)
        cc.export(
            "push",
            "void(i8)")(
            push)
        # b1: bool, i4: int32, i8: int64, double: f8, [:], [:, :]
        cc.compile()
        exit()

    if sys.argv[-1] != "-p":  # mean: pure python mode
        from numba_rbst import randInt, lower_bound, update, split, merge, push

    _test()
    r = RBST()
    if 1:
        t = time.perf_counter()
        for i in range(100000):
            r.insert(0)
        t = time.perf_counter() - t
        print(f"{t:.2f}")  # 100000 => 0.91sec
        # with lprof 22.91sec
