"""
illustration logic
"""
import numpy as np


def debug(*x):
    import sys
    print(*x, file=sys.stderr)


def bar(N, hints, is0=None, is1=None):
    """
    >>> bar(10, [9])
    .########.

    >>> bar(10, [5, 3])
    .####..##.

    >>> bar(10, [5, 4])
    #####x####

    >>> bar(10, [2, 2, 3])
    .#..#..##.

    >>> is1 = np.array([1,0,0,0,0,0,0,0,0,0,0])

    >>> bar(10, [9], is1=is1)
    #########x

    >>> bar(10, [5, 3], is1=is1)
    #####x.##.

    """
    cache = {}
    # possibility
    can0 = np.zeros(N + 1, dtype=np.int)
    can1 = np.zeros(N + 1, dtype=np.int)
    # constraint
    if is0 is None:
        is0 = np.zeros(N + 1, dtype=np.int)
    if is1 is None:
        is1 = np.zeros(N + 1, dtype=np.int)

    slack = N - (sum(hints) + len(hints) - 1)

    def foo(start, slack, hints):
        # debug(": start, slack, hints", start, slack, hints)
        key = (start, len(hints))
        if key in cache:
            return cache[key]
        if not hints:
            if np.all(is1[start:] == 0):
                can0[start:] = 1
                cache[key] = True
                return True
            cache[key] = False
            return False

        ret = False
        for i in range(slack + 1):
            if (
                np.all(is1[start:start + i] == 0) and
                np.all(is0[start + i:start + i + hints[0]] == 0) and
                is1[start + i + hints[0]] == 0
            ):

                if foo(start + i + hints[0] + 1, slack - i, hints[1:]):
                    can0[start:start + i] = 1
                    can1[start + i:start + i + hints[0]] = 1
                    can0[start + i + hints[0]] = 1
                    ret = True

        cache[key] = ret
        return ret

    foo(0, slack, hints)
    print("".join(".x#"[can0[i] - can1[i]] for i in range(N)))
    # print(can0[:-1])
    # print(can1[:-1])


def _test():
    import doctest
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
            doctest.run_docstring_examples(g[k], g, name=k)


if __name__ == "__main__":
    import sys
    if sys.argv[-1] == "-t":
        print("testing")
        _test()
        sys.exit()
