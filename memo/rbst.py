#!/usr/bin/env python3
# Randomized Binary Search Tree
# derived from https://qiita.com/drken/items/1b7e6e459c24a83bb7fd


import numpy as np
import time


def dp(*x):  # debugprint
    if RBST.debug:
        print(*x)


try:
    profile
except:
    def profile(f): return f

SUM_UNITY = 0


@profile
def update(lefts, rights, vals, sizes, sums, node):
    sizes[node] = sizes[lefts[node]] + sizes[rights[node]] + 1
    sums[node] = sums[lefts[node]] + sums[rights[node]] + vals[node]
    # add extra code here
    return node


def push(node):
    if not node:
        return
    # add extra code here


@profile
def lower_bound(lefts, rights, vals, sizes, node, val):
    # dp("lowerbound: node, val", node, val)

    push(node)
    if not node:
        # dp("lowerbound result: 0")
        return 0
    if val <= vals[node]:
        # dp("val <= vals[node]")
        ret = lower_bound(lefts, rights, vals, sizes,  lefts[node], val)
        # dp("lowerbound result: ret", ret)
        return ret
    # dp("val > vals[node]")
    ret = sizes[lefts[node]] + 1
    ret += lower_bound(lefts, rights, vals, sizes,  rights[node], val)
    # dp("lowerbound result: ret", ret)
    return ret


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


@profile
def merge(
        lefts, rights, vals, sizes, sums,
        left, right, t=np.array([123456789, 362436069, 521288629, 88675123])):
    # dp("merge: left,right", left, right)
    push(left)
    push(right)
    if not left or not right:
        if left:
            return left
        return right
    # if randint(0, left.size + right.size) < left.size:
    if randInt(t) % (sizes[left] + sizes[right]) < sizes[left]:
        rights[left] = merge(
            lefts, rights, vals, sizes, sums,
            rights[left], right)
        return update(lefts, rights, vals, sizes, sums, left)
    else:
        lefts[right] = merge(
            lefts, rights, vals, sizes, sums,
            left, lefts[right])
        return update(lefts, rights, vals, sizes, sums, right)


@profile
def split(lefts, rights, vals, sizes, sums, node, k):
    "split tree into [0, k) and [k, n)"
    # dp("split: node, k", node, k)
    push(node)
    if not node:
        RBST.ret_left = 0
        RBST.ret_right = 0
        return
    if k <= sizes[lefts[node]]:
        # dp("split left")
        split(lefts, rights, vals, sizes, sums,
              lefts[node], k)
        lefts[node] = RBST.ret_right
        RBST.ret_right = update(lefts, rights, vals, sizes, sums, node)
        return
    else:
        # dp("split right")
        split(lefts, rights, vals, sizes, sums,
              rights[node], k - sizes[lefts[node]] - 1)
        rights[node] = RBST.ret_left
        RBST.ret_left = update(lefts, rights, vals, sizes, sums, node)
        return


class RBST:
    debug = False
    ret_left = None
    ret_right = None

    def __init__(self, node=None):
        self.root = node
        MAX_NODE_ID = 400_000
        self.vals = [SUM_UNITY] * MAX_NODE_ID
        self.sizes = [1] * MAX_NODE_ID
        self.sums = [SUM_UNITY] * MAX_NODE_ID
        self.lefts = [0] * MAX_NODE_ID
        self.rights = [0] * MAX_NODE_ID
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

            self.root, add.root)

    def split(self, k):
        split(
            self.lefts, self.rights, self.vals, self.sizes, self.sums,

            self.root, k)
        self.root = RBST.ret_left
        return RBST.ret_right

    def insert(self, val):
        split(
            self.lefts, self.rights, self.vals, self.sizes, self.sums,

            self.root, self.lower_bound(val))
        r = merge(
            self.lefts, self.rights, self.vals, self.sizes, self.sums,

            RBST.ret_left, self.new_node(val))
        # dp("merge(x1, Node(val)): ", r)
        r = merge(
            self.lefts, self.rights, self.vals, self.sizes, self.sums,

            r, RBST.ret_right)
        # dp("merge(r, x2): ", r)
        self.root = r

    def erase(self, val):
        if self.count(val) == 0:
            return
        split(
            self.lefts, self.rights, self.vals, self.sizes, self.sums,
            self.root, self.lower_bound(val))
        lhs = RBST.ret_left
        split(
            self.lefts, self.rights, self.vals, self.sizes, self.sums,

            RBST.ret_right, 1)
        rhs = RBST.ret_right
        self.root = merge(
            self.lefts, self.rights, self.vals, self.sizes, self.sums,

            lhs, rhs)

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
        # b1: bool, i4: int32, i8: int64, double: f8, [:], [:, :]
        cc.compile()
        exit()
    from numba_rbst import randInt

    _test()
    r = RBST()
    if 1:
        t = time.perf_counter()
        for i in range(100000):
            r.insert(0)
        t = time.perf_counter() - t
        print(t)  # 100000 => 2.84sec
        # with lprof 22.91sec
