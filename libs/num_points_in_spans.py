def numPointsInSpans(spans):
    """
    ARC112B
    >>> numPointsInSpans([(1, 3)])
    3
    >>> numPointsInSpans([(1, 3), (5, 7)])
    6
    >>> numPointsInSpans([(1, 3), (3, 5)])
    5
    >>> numPointsInSpans([(1, 3), (2, 5)])
    5
    """
    timeline = []
    for start, end in spans:
        assert start <= end
        timeline.append((start, 0, 1))
        timeline.append((end, 1, -1))
    prevStart = None
    value = 0
    ret = 0
    for position, _, diff in sorted(timeline):
        prevValue = value
        value += diff
        if prevValue == 0 and value > 0:
            prevStart = position
        elif prevValue > 0 and value == 0:
            ret += position - prevStart + 1
    return ret
