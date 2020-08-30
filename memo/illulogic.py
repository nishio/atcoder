"""
illustration logic
"""
import numpy as np


def debug(*x):
    import sys
    print(*x, file=sys.stderr)


def estimate(N, hints):
    slack = N - (sum(hints) + len(hints) - 1)
    from math import log
    return log(slack + 1) * len(hints)


def solve(N, hints, is0, is1):
    cache = {}
    # possibility
    can0 = np.zeros(N + 1, dtype=np.int)
    can1 = np.zeros(N + 1, dtype=np.int)
    slack = N - (sum(hints) + len(hints) - 1)

    def recur(start, slack, hints):
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

                if recur(start + i + hints[0] + 1, slack - i, hints[1:]):
                    can0[start:start + i] = 1
                    can1[start + i:start + i + hints[0]] = 1
                    can0[start + i + hints[0]] = 1
                    ret = True

        cache[key] = ret
        return ret

    recur(0, slack, hints)

    for i in range(N):
        v = can0[i] - can1[i]
        if v == 1:
            is0[i] = 1
        if v == -1:
            is1[i] = 1


def test1d(N, hints, is0=None, is1=None):
    """
    >>> test1d(10, [9])
    .########.

    >>> test1d(10, [5, 3])
    .####..##.

    >>> test1d(10, [5, 4])
    #####x####

    >>> test1d(10, [2, 2, 3])
    .#..#..##.

    >>> is1 = np.array([1,0,0,0,0,0,0,0,0,0,0])

    >>> test1d(10, [9], is1=is1.copy())
    #########x

    >>> test1d(10, [5, 3], is1=is1.copy())
    #####x.##.
    """
    if is0 is None:
        is0 = np.zeros(N + 1, dtype=np.int)
    if is1 is None:
        is1 = np.zeros(N + 1, dtype=np.int)
    solve(N, hints, is0, is1)

    m = is0[:-1] - is1[:-1]
    print("".join(".x#"[x] for x in m))


def render2d(is0, is1, chars=".x#"):
    m = is0[:-1, :-1] - is1[:-1, :-1]
    for line in m:
        print("".join(chars[x] for x in line))


def test2d():
    """
    >>> test2d()
    _#_#___##_
    _###__#__#
    #_#_#_#_##
    ##_##_#_##
    _###__#_##
    _#####_###
    #########_
    #_#_#####_
    #_#_####__
    _#####____
    """
    W = 10
    H = 10
    is0 = np.zeros((W + 1, H + 1), dtype=np.int)
    is1 = np.zeros((W + 1, H + 1), dtype=np.int)
    h_hints = [
        [1, 1, 2],
        [3, 1, 1],
        [1, 1, 1, 1, 2],
        [2, 2, 1, 2],
        [3, 1, 2],
        [5, 3],
        [9],
        [1, 1, 5],
        [1, 1, 4],
        [5],
    ]
    for i in range(H):
        # print(estimate(W, h_hints[i]))
        solve(W, h_hints[i], is0[i], is1[i])
    # render2d(is0, is1)
    # print()
    v_hints = [
        [2, 3],
        [2, 4, 1],
        [2, 6],
        [2, 4, 1],
        [2, 5],
        [5],
        [4, 3],
        [1, 4],
        [1, 6],
        [5]
    ]
    for i in range(W):
        solve(H, v_hints[i], is0[:, i], is1[:, i])
    # render2d(is0, is1)
    # print()

    while is0.sum() + is1.sum() < H * W:
        for i in range(H):
            solve(W, h_hints[i], is0[i], is1[i])
        for i in range(W):
            solve(H, v_hints[i], is0[:, i], is1[:, i])
    render2d(is0, is1, chars=" _#")


def _test():
    import doctest
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
            doctest.run_docstring_examples(g[k], g, name=k)
    test2d()


if __name__ == "__main__":
    import sys
    if sys.argv[-1] == "-t":
        print("testing")
        _test()
        sys.exit()
