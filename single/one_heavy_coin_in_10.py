"""
One heavy coin in 10 coins
"""
from math import log
import itertools
possible = list(itertools.combinations(range(10), 2))
N = len(possible)


def first():
    for i in range(1, 6):
        lhs = range(i)
        rhs = range(i, 2 * i)
        yield lhs, rhs


def make_split(N):
    for size in range(1, N // 2 + 1):
        for lhs in itertools.combinations(range(N), size):
            rcandidate = [i for i in range(lhs[0] + 1, N) if i not in lhs]
            for rhs in itertools.combinations(rcandidate, size):
                yield (lhs, rhs)


def foo(possible=possible, split=first()):
    score = 0
    ret = None
    for lhs, rhs in split:
        count = {-1: [], 0: [], 1: []}
        for p in possible:
            s = 0
            for x in p:
                if x in lhs:
                    s -= 1
                elif x in rhs:
                    s += 1
            s = min(max(s, -1), 1)
            count[s].append(p)

        ls = [len(x) for x in count.values()]
        info = -sum([x / N * log(x / N) / log(2) if x else 0.0 for x in ls])
        if info > score:
            score = info
            best_split = (tuple(lhs), tuple(rhs))
            best_next = count

    # print(f"{score=:.2f}, {ret=}")
    print(best_split)
    print("left:", tuple(best_next[-1]))
    print("equal:", tuple(best_next[0]))
    print("right:", tuple(best_next[1]))
    return best_next


t1 = foo()
t2 = foo(t1[-1], make_split(10))
t3 = foo(t2[-1], make_split(10))
t4 = foo(t3[0], make_split(10))

t2 = foo(t1[0], make_split(10))
t3 = foo(t2[-1], make_split(10))
t3 = foo(t2[0], make_split(10))
