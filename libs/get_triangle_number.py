def getTriangleNumber(n, when_negative=None):
    # ARC112A
    if n < 0:
        if when_negative is None:
            raise AssertionError("arg should not be negative")
        return when_negative
    return n * (n + 1) // 2
