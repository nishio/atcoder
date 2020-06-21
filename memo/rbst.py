#!/usr/bin/env python3
# Randomized Binary Search Tree
# derived from https://qiita.com/drken/items/1b7e6e459c24a83bb7fd


import time
from random import randint, seed
seed(42)


def dp(*x):  # debugprint
    if RBST.debug:
        print(*x)


SUM_UNITY = 0


class Node:
    """
        NODE * left, *right
        VAL val
        // the value of the node
        int size
        // the size of the subtree
        VAL sum
        // the value-sum of the subtree
    """

    def __init__(self, v=None):
        # no args
        if v == None:
            self.val = SUM_UNITY
            self.size = 1
            self.sum = SUM_UNITY
            self.left = self.right = None
        else:
            self.val = v
            self.size = 1
            self.sum = v
            self.left = self.right = None

    def push(self):
        pass

    def update(self):
        pass

    def __repr__(self):
        left = repr(self.left) if self.left else "x"
        right = repr(self.right) if self.right else "x"
        v = repr(self.val)
        return f"[{left} _{v}_ {right}]"


def size(node):
    if not node:
        return 0
    return node.size


def rbst_sum(node):
    if not node:
        return SUM_UNITY
    return node.sum


def update(node):
    node.size = size(node.left) + size(node.right) + 1
    node.sum = rbst_sum(node.left) + rbst_sum(node.right) + node.val
    node.update()
    return node


def push(node):
    if not node:
        return
    node.push()


def lower_bound(node, val):
    if RBST.debug:
        dp("lowerbound: node, val", node, val)

    push(node)
    if not node:
        dp("lowerbound result: 0")
        return 0
    if val <= node.val:
        dp("val <= node.val")
        ret = lower_bound(node.left, val)
        dp("lowerbound result: ret", ret)
        return ret
    dp("val > node.val")
    ret = size(node.left) + lower_bound(node.right, val) + 1
    dp("lowerbound result: ret", ret)
    return ret


def upper_bound(node, val):
    push(node)
    if not node:
        return 0
    if val >= node.val:
        return size(node.left) + upper_bound(node.right, val) + 1
    return upper_bound(node.left, val)


def get(node, k):
    "k: 0-origin"
    push(node)
    if not node:
        return -1
    if k == size(node.left):
        return node.val
    if k < size(node.left):
        return get(node.left, k)
    return get(node.right, k - size(node.left) - 1)


def merge(left, right):
    dp("merge: left,right", left, right)
    push(left)
    push(right)
    if not left or not right:
        if left:
            return left
        return right
    if randint(0, left.size + right.size) < left.size:
        left.right = merge(left.right, right)
        return update(left)
    else:
        right.left = merge(left, right.left)
        return update(right)


def split(node, k):
    "split tree into [0, k) and [k, n)"
    dp("split: node, k", node, k)
    push(node)
    if not node:
        ret = (node, node)
        dp("split: ret", ret)
        return ret
    if k <= size(node.left):
        dp("split left")
        x1, x2 = split(node.left, k)
        node.left = x2
        ret = (x1, update(node))
        dp("split: ret", ret)
        return ret
    else:
        dp("split right")
        x1, x2 = split(node.right, k - size(node.left) - 1)
        node.right = x1
        ret = (update(node), x2)
        dp("split: ret", ret)
        return ret


class RBST:
    debug = False

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
        x1, x2 = split(self.root, k)
        self.root = x1
        return x2

    def insert(self, val):
        x1, x2 = split(self.root, self.lower_bound(val))
        if RBST.debug:
            print(x1, x2)
        r = merge(x1, Node(val))
        dp("merge(x1, Node(val)): ", r)
        r = merge(r, x2)
        dp("merge(r, x2): ", r)
        self.root = r

    def erase(self, val):
        if self.count(val) == 0:
            return
        x1, x2 = split(self.root, self.lower_bound(val))
        self.root = merge(x1, split(x2, 1)[1])

    def print(self):
        print("{ ", end="")
        print_node(self.root)
        print("}")

    def __repr__(self):
        return repr(node_as_list(self.root))


def node_as_list(node):
    if not node:
        return []
    s = [node.val]
    if node.left:
        s = node_as_list(node.left) + s
    if node.right:
        s = s + node_as_list(node.right)
    return s


def print_node(node):
    if not node:
        return
    print_node(node.left)
    print(node.val, end=" ")
    print_node(node.right)


def print_node_as_tree(node, indent=0):
    if not node:
        print(" " * indent + "x")
        return
        # return
    print_node_as_tree(node.right, indent + 1)
    print(" " * indent + str(node.val))
    print_node_as_tree(node.left, indent + 1)


def main():
    """
    >>> r = RBST()
    >>> r
    []
    >>> r.insert(2)
    >>> r
    [2]
    >>> print_node_as_tree(r.root)
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


if __name__ == "__main__":
    import sys
    if sys.argv[-1] == "-c":
        # numba compile
        print("compiling")
        from numba.pycc import CC
        cc = CC('numba_rbst')
        # cc.export('randInt', 'i8()')(main)
        # b1: bool, i4: int32, i8: int64, double: f8, [:], [:, :]
        cc.compile()
        exit()
    #from numba_rbst import randInt
    _test()
    r = RBST()
    if 1:
        t = time.perf_counter()
        for i in range(100000):
            r.insert(0)
        t = time.perf_counter() - t
        print(t)  # 100000 => 6.16sec
        # 10000 => 0.52sec
