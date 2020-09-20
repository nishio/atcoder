"""
ABC179 D
"""


def accum_generation(N):
    """
    >>> accum_generation(10)
    [1, 0, 1, 1, 1, 2, 2, 3, 4, 5]
    """
    value = [0] * (N + 10)
    accum = [0] * (N + 10)
    value[0] = 1
    accum[0] = 1
    for pos in range(1, N):
        ret = (accum[pos - 2] - accum[pos - 4])
        value[pos] = ret
        accum[pos] = accum[pos - 1] + ret

    return value[:N]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
