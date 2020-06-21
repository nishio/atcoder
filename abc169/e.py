TEST = False

if not TEST:
    N = int(input())
    AS = []
    BS = []
    for i in range(N):
        A, B = [int(x) for x in input().split()]
        AS.append(A)
        BS.append(B)


def getBound(AS, BS):
    """
    >>> getBound([0, 1], [1, 2])
    1 3 3
    >>> getBound([0, 0], [1, 2])
    1 3 3
    >>> getBound([0, 1, 2], [1, 2, 3])
    1 2 2
    >>> getBound([0, 1, 2], [1, 3, 3])
    1 3 3
    >>> getBound([0, 0, 1], [2, 3, 3])
    0 3 4
    """
    N = len(AS)
    AS2 = AS[:]
    AS2.sort()

    BS2 = BS[:]
    BS2.sort()
    if N % 2 == 0:
        lower = AS2[N // 2 - 1] + AS2[N // 2]
        upper = BS2[N // 2 - 1] + BS2[N // 2]
        result = upper - lower + 1
    else:
        lower = AS2[N // 2]
        upper = BS2[N // 2]
        result = upper - lower + 1
    if TEST:
        print(lower, upper, result)
    else:
        return result


def _test():
    import doctest
    doctest.testmod()


if TEST:
    _test()
else:
    print(getBound(AS, BS))
