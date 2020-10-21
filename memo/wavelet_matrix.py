"""
Wavelet Matrix

The Wavelet Matrix: An Efficient Wavelet Tree for Large Alphabets
https://www.semanticscholar.org/paper/The-wavelet-matrix%3A-An-efficient-wavelet-tree-for-Claude-Navarro/17d8debc499dc74603edc061bded70b622571f91?p2df
"""


def access_naive(s, i):
    """
    access(S, i) returns S[i].
    """
    return s[i]


def access(s, i):
    pass


def rank_naive(s, a, i):
    """
    rank_a(S, i) returns the number of occurrences of symbol a in S[1, i].
    """
    return s[:i].count(a)


class NaiveBitVector:
    """
    >>> NaiveBitVector([1, 1, 1, 1]).rank(3)
    3
    """

    def __init__(self, value):
        self.value = value

    def rank(self, i):
        return rank_naive(self.value, 1, i)


class AccumBitVector:
    """
    >>> AccumBitVector([1, 1, 1, 1]).rank(3)
    3
    """

    def __init__(self, value):
        self.value = value
        self.accum = [0] * len(value)
        for i in range(len(value)):
            self.accum[i] = self.accum[i - 1] + value[i]

    def rank(self, i):
        return self.accum[i - 1]


def _rank(l, a, i, p):
    """
    _rank(0, a, i, 0) == rank_a(S, i)
    """


def select(s, a, i):
    """
    select_a(S, j) returns the position in S of the j-th occurrence of symbol a.
    """


def construct(s, maxvalue, to_print=False, to_return=True):
    """
    >>> construct([5, 4, 5, 5, 2, 1, 5, 6, 1, 3, 5, 0], 6, to_print=True, to_return=False)
    [1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0]
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0]
    [1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0]
    num0: 4
    start_positions: [0, 4, 2, 11, 1, 6, 3]
    """
    a = maxvalue.bit_length()
    # debug(a, msg=":a")

    bs = []

    for iter in range(a):
        mask = 1 << (a - 1 - iter)
        bs.append([])
        b = bs[-1]
        for x in s:
            b.append(int(mask & x > 0))
        # debug(b, msg=f"{iter}:b")

        # stable sort
        s1 = []
        s0 = []
        for i in range(len(s)):
            if b[i]:
                s1.append(s[i])
            else:
                s0.append(s[i])
        s = s0 + s1
        # debug(s, msg=f"{iter}:s")

    num0 = len(s0)
    # debug(num0, msg=":num0")
    start_positions = [s.index(x) for x in range(maxvalue + 1)]
    # debug(start_positions, msg=":start_positions")
    if to_print:
        for b in bs:
            print(b)
        print("num0:", num0)
        print("start_positions:", start_positions)
    if to_return:
        return WavelerMatrix(bs, num0, start_positions)


class WavelerMatrix:
    def __init__(self, bs, num0, start_positions, BitVector=AccumBitVector):
        self.bs = [BitVector(b) for b in bs]
        self.num0 = num0
        self.start_positions = start_positions

# --- end of library ---


def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def _test():
    import doctest
    print("testing")
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
            doctest.run_docstring_examples(g[k], g, name=k)


if __name__ == "__main__":
    import sys
    input = sys.stdin.buffer.readline
    read = sys.stdin.buffer.read
    if sys.argv[-1] == "-t":
        _test()
        sys.exit()
    # main()
