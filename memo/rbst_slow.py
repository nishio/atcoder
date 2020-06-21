#!/usr/bin/env python3
# Randomized Binary Search Tree
# derived from https://qiita.com/drken/items/1b7e6e459c24a83bb7fd


import time


def dp(*x):  # debugprint
    if RBST.debug:
        print(*x)


def randInt(t=[123456789, 362436069, 521288629, 88675123]):
    tx, ty, tz, tw = t
    tt = tx ^ (tx << 11)
    t[0] = ty
    t[1] = tz
    t[2] = tw
    t[3] = tw = (tw ^ (tw >> 19)) ^ (tt ^ (tt >> 8))
    return tw


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
        return repr(self.val)


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
        return 0
    if val <= node.val:
        dp("val <= node.val")
        ret = lower_bound(node.left, val)
        dp("lowerbound result: ret", ret)
        return ret
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
    push(left)
    push(right)
    if not left or not right:
        if left:
            return left
        return right
    if randInt() % (left.size + right.size) < left.size:
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
        return (node, node)
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
        self.root = merge(merge(x1, Node(val)), x2)

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
        if not self.root:
            return "[]"
        s = repr(self.root)
        if self.root.left:
            s = f"{self.root.left} {s}"
        if self.root.right:
            s = f"{s} {self.root.right}"
        return f"[{s}]"


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
    [1 2]
    >>> print_node_as_tree(r.root)
     x
    2
      x
     1
      x
    >>> r.insert(3)
    >>> r
    [1 2 3]
    >>> print_node_as_tree(r.root)
      x
     3
      x
    2
      x
     1
      x
    >>> r.erase(2)
    >>> print_node_as_tree(r.root)
     x
    3
      x
     1
      x
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
    _test()
    r = RBST()
    t = time.perf_counter()
    for i in range(10000):
        r.insert(0)
    t = time.perf_counter() - t
    print(t)  # => 4.5sec
