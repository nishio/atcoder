from string import ascii_lowercase


def solve(N):
    """
    >>> solve(2)
    b
    >>> solve(27)
    aa
    >>> solve(703)
    aaa
    """
    q = N
    ret = ""
    while True:
        q, r = divmod(q - 1, 26)
        ret = ascii_lowercase[r] + ret
        if q == 0:
            print(ret)
            return


def main():
    N = int(input())
    solve(N)


def _test():
    import doctest
    doctest.testmod()


if __name__ == "__main__":
    import sys
    argv = sys.argv
    if len(sys.argv) == 1:
        # no option
        main()
    elif sys.argv[1] == "-t":
        _test()
    else:
        input = open(sys.argv[1]).buffer.readline
