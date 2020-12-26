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


# --- end of library ---

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
