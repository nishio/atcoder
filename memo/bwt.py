def cyclic_shift(s, i):
    return s[i:] + s[:i]


def unsorted_cyclic_shifts(s, to_print=False, to_return=True, sep=" "):
    """
    >>> unsorted_cyclic_shifts("CTCTGC$", to_print=True, to_return=False)
    0 C T C T G C $
    1 T C T G C $ C
    2 C T G C $ C T
    3 T G C $ C T C
    4 G C $ C T C T
    5 C $ C T C T G
    6 $ C T C T G C
    """
    ret = [cyclic_shift(s, i) for i in range(len(s))]
    if to_print:
        for i, v in enumerate(ret):
            print(i, *v, sep=sep)
    if to_return:
        return ret


def sorted_cyclic_shifts(s, to_print=False, to_return=True, sep=" "):
    """
    >>> sorted_cyclic_shifts("CTCTGC$", to_print=True, to_return=False)
    0 $ C T C T G C
    1 C $ C T C T G
    2 C T C T G C $
    3 C T G C $ C T
    4 G C $ C T C T
    5 T C T G C $ C
    6 T G C $ C T C
    """
    ret = unsorted_cyclic_shifts(s)
    ret.sort()
    if to_print:
        for i, v in enumerate(ret):
            print(i, *v, sep=sep)
    if to_return:
        return ret


def bwt_naive(s):
    """
    >>> bwt_naive("CTCTGC$")
    'CG$TTCC'
    """
    return "".join(row[-1] for row in sorted_cyclic_shifts(s))


def debug(*x):
    import sys
    print(*x, file=sys.stderr)


def inverse_bwt_naive(last):
    """
    >>> inverse_bwt_naive(bwt_naive("CTCTGC$"))
    'CTCTGC$'
    """
    first = list(sorted(last))
    for _i in range(len(last) - 1):
        # cyclic shift: last letter comes before first
        first = [f"{l}{f}" for f, l in zip(first, last)]
        # now `first` is shuffle of matrix. Sort it.
        first.sort()
        # debug("first", first)
    ret = cyclic_shift(first[0], 1)
    # debug("ret", ret)
    return ret


def get_C(s, i):
    """
    get number of smaller letters than s[i].
    equiv. first occurence of s[i] in sorted s.
    """
    c = s[i]
    s = list(sorted(s))
    return s.index(c)


def get_rank(s, i):
    """
    get number of occurence of s[i] before i.
    """
    c = s[i]
    return s[:i].count(c)


def get_lf_mapping(last):
    """
    efficient impl. of inverse_bwt
    https://tech.preferred.jp/ja/blog/burrows-wheeler-transform-lf-mapping/
    >>> get_lf_mapping(bwt_naive("CTCTGC$"))
    [1, 4, 0, 5, 6, 2, 3]
    """
    ret = [
        get_C(last, i) + get_rank(last, i)
        for i in range(len(last))
    ]
    return ret


def inverse_bwt_lf(last):
    """
    >>> inverse_bwt_lf(bwt_naive("CTCTGC$"))
    'CTCTGC$'
    """
    lf = get_lf_mapping(last)
    cur = 0
    ret = []
    for _i in range(len(last)):
        ret.append(last[cur])
        cur = lf[cur]

    ret.reverse()
    ret = cyclic_shift(ret, 1)
    # debug("ret", ret)
    return "".join(ret)


def _test():
    import doctest
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
        print("testing")
        _test()
        sys.exit()
    main()
