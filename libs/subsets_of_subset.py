"""
all subsets of given subset
"""


def subsets_of_subset(subset):
    s = subset
    superset = subset
    while True:
        yield s
        s = (s - 1) & superset
        if s == superset:
            break


# --- end of library ---
def debugprint(g):
    for x in g:
        print(f"{x:06b}")


TEST_1 = """
>>> debugprint(subsets_of_subset(0b010101))
010101
010100
010001
010000
000101
000100
000001
000000
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
