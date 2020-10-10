"""
Deletable list (doubly linked list with zero-fill array)

NOTICE: the first item is sentinel, can not delete.

>>> d = Deletable(list(range(10)))
>>> list(d.iter())
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> d.delete(5)
>>> list(d.iter())
[0, 1, 2, 3, 4, 6, 7, 8, 9]
"""


class Deletable:
    def __init__(self, items):
        self.items = items
        self.size = len(items)
        self.prev = [0] * (self.size + 1)
        self.next = [0] * (self.size + 1)

    def delete(self, pos):
        self.prev[pos + 1 + self.next[pos]] += self.prev[pos] + 1
        self.next[pos - 1 - self.prev[pos]] += self.next[pos] + 1
        self.next[pos] = -1  # means "deleted"

    def is_deleted(self, pos):
        return self.next[pos] < 0

    def iter(self, start=0):
        pos = start
        if self.is_deleted(start):
            pos = self.next[start - 1] + start

        while pos < self.size:
            yield self.items[pos]
            pos += self.next[pos] + 1

    def debug(self):
        print(self.items)
        print(self.next)
        print(self.prev)
# --- end of library ---


TEST_T1 = """
>>> d = Deletable(list(range(10)))
>>> list(d.iter())
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> d.delete(5)
>>> list(d.iter())
[0, 1, 2, 3, 4, 6, 7, 8, 9]

>>> d.delete(4)
>>> list(d.iter())
[0, 1, 2, 3, 6, 7, 8, 9]

>>> d.delete(6)
>>> list(d.iter())
[0, 1, 2, 3, 7, 8, 9]

>>> d.delete(8)
>>> list(d.iter())
[0, 1, 2, 3, 7, 9]
"""

TEST_T2 = """
>>> d = Deletable([0])
>>> d.delete(0)
>>> list(d.iter())
[]
>>> d = Deletable([0, 1])
>>> d.delete(0)
>>> list(d.iter())
[1]
"""


def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def random_test():
    from random import random, seed
    N = 10
    for i in range(100):
        seed(i)
        xs = list(range(N))
        d = Deletable(list(range(N)))
        while xs:
            x = int(random() * N)
            if x in xs:
                # debug(x, msg="delete:x")
                xs.remove(x)
                assert not d.is_deleted(x)
                d.delete(x)
                # debug(xs, list(d.iter()), msg=":xs, list(d.iter())")
                assert xs == list(d.iter())
    print("ok")


def _test():
    import doctest
    print("testing")
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
            doctest.run_docstring_examples(g[k], g, name=k)


def main():
    """
    >>> random_test()
    ok
    """


if __name__ == "__main__":
    import sys
    input = sys.stdin.buffer.readline
    read = sys.stdin.buffer.read
    if sys.argv[-1] == "-t":
        _test()
        sys.exit()
    main()
