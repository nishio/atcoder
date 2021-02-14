# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve_WA(B, C):
    # B-C/2 .. B
    ret = 1 + C // 2
    if C >= 1:
        # -B-(C-1)/2 .. -B
        ret += 1 + (C - 1) // 2
        # -B .. -B + (C-1)/2
        ret += (C - 1) // 2
    if C >= 2:
        # B .. B + (C-2)//2
        ret += (C - 2) // 2
    return ret


def solve_WA2(B, C):
    if B < 0:
        B = -B
    # B-C/2 .. B
    s1 = B - C // 2
    e1 = B
    if C >= 1:
        # -B-(C-1)/2 .. -B
        s2 = -B - (C - 1) // 2
        # -B .. -B + (C-1)/2
        e2 = -B + (C - 1) // 2
    if C >= 2:
        # B .. B + (C-2)//2
        e1 = B + (C - 2) // 2

    ret = e1 - s1 + 1 + e2 - s2 + 1
    if s1 <= e2:
        # overlap
        ret -= e2 - s1 + 1
    return ret


def numPointsInSpans(spans):
    """
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


def solve(B, C):
    if C == 0:
        return 1

    spans = [(B - C // 2, B)]
    if C >= 1:
        spans.append((-B-(C-1)//2, -B))
        spans.append((-B, -B + (C - 1) // 2))
    if C >= 2:
        spans.append((B, B + (C - 2) // 2))

    return numPointsInSpans(spans)


def blute(B, C):
    from heapq import heappush, heappop
    q = [(-C, B)]
    used = set()
    ret = set([B])
    while q:
        nc, b = heappop(q)
        if nc > 0:
            continue
        ret.add(b)
        if nc == 0:
            continue
        x = (nc + 1, -b)
        if x not in used:
            used.add(x)
            heappush(q, x)
        x = (nc + 2, b - 1)
        if x not in used:
            used.add(x)
            heappush(q, x)
    blute.ret = ret
    return len(ret)


def main():
    B, C = map(int, input().split())
    print(solve(B, C))


def random_test():
    for B in range(-10, 11):
        for C in range(40):
            if blute(B, C) != solve(B, C):
                debug(B, C, solve(B, C), blute(B, C), msg=":B,C,solve,blute")


# tests
T1 = """
11 2
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
3
"""
T2 = """
0 4
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
4
"""
T3 = """
112 20210213
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
20210436
"""
T4 = """
-211 1000000000000000000
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
1000000000000000422
"""


def _test():
    import doctest
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
            print(k)
            doctest.run_docstring_examples(g[k], g, name=k)


def as_input(s):
    "use in test, use given string as input file"
    import io
    f = io.StringIO(s.strip())
    g = globals()
    g["input"] = lambda: bytes(f.readline(), "ascii")
    g["read"] = lambda: bytes(f.read(), "ascii")


if __name__ == "__main__":
    import sys
    input = sys.stdin.buffer.readline
    read = sys.stdin.buffer.read
    sys.setrecursionlimit(10 ** 6)
    if sys.argv[-1] == "-t":
        print("testing")
        _test()
        sys.exit()
    main()
    sys.exit()

# end of snippets/main.py
