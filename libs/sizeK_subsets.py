"""
all size K subsets of size N superset
"""


def all_sizeK_subsets(N, K):
    x = (1 << K) - 1
    FULL = 1 << N
    while x < FULL:
        yield x
        # example x = 00110110
        a = x & -x  # 00000010: rightmost one
        b = x + a   # 00111000
        c = x & ~b  # 00000110: rightmost one block
        d = c // a  # 00000011: remove trailing zeros
        e = d >> 1  # 00000001
        x = e | b   # 00111001

# --- end of library ---
# included from libs/bin_to_str.py


def bin_to_str(x, digits=16):
    """
    >>> bin_to_str(10, 6)
    '001010'
    """
    format = "{x:0%db}" % digits
    return format.format(x=x)


def bin_to_revstr(x, digits=16):
    """
    >>> bin_to_revstr(10, 6)
    '010100'
    """
    return "".join(reversed(bin_to_str(x, digits)))
# end of libs/bin_to_str.py


def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def debugprint(g):
    for x in g:
        print(bin_to_str(x, 5))


TEST_1 = """
>>> debugprint(all_sizeK_subsets(5, 2))
00011
00101
00110
01001
01010
01100
10001
10010
10100
11000
"""


def _test():
    import doctest
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
            print(k)
            doctest.run_docstring_examples(g[k], g, name=k)


if __name__ == "__main__":
    import sys
    input = sys.stdin.buffer.readline
    read = sys.stdin.buffer.read
    if sys.argv[-1] == "-t":
        _test()
        sys.exit()
