from heapq import _siftdown
from heapq import *

added = []
removed = []
# add
heappush(added, 1)
heappush(added, 2)
# remove
heappush(removed, 1)
# get top
while removed and added[0] == removed[0]:
    heappop(added)
    heappop(removed)

print(added[0])  # => 2


N = 2
M = 2
items = [[] for _ in range(N)]
position = [-1] * M


def put(id, pos):
    heappush(items[pos], id)
    position[id] = pos


move = put


def top(pos):
    q = items[pos]
    while q:
        id = q[0]
        if position[id] != pos:
            heappop(q)
            continue
        return id
    return None


put(0, 0)
put(1, 0)

move(0, 1)
print(top(0))  # => 1
move(0, 0)
print(top(0))  # => 0
move(0, 1)
print(top(0))  # => 1

N = 2
values = [None] * N
lastUpdate = [0] * N
queue = []
time = 0


def update(pos, value):
    global time
    time += 1
    values[pos] = value
    heappush(queue, (value, pos, time))
    lastUpdate[pos] = time


def top():
    while queue:
        value, pos, time = queue[0]
        if time == lastUpdate[pos]:
            return value
        heappop(queue)
    return None


update(0, 42)
print(top())  # => 42
update(1, 43)
print(top())  # => 42
update(0, 44)
print(top())  # => 43

queue = [1, 2, 3]
K = 1
queue[K] = -1
_siftdown(queue, 0, K)
print(queue)  # => [-1, 1, 3]


def foo():
    from random import shuffle
    xs = list(range(10))
    shuffle(xs)
    upper = []
    lower = []
    for i, x in enumerate(xs):
        if i % 2 == 0:
            heappush(upper, x)
        else:
            heappush(lower, -x)
            print(upper, lower)
            if -lower[0] > upper[0]:
                l = -lower[0]
                u = -upper[0]
                heapreplace(lower, u)
                heapreplace(upper, l)
                print(upper, lower)
    print(upper[0], -lower[0])


def foo2():
    from random import shuffle
    xs = list(range(100))
    shuffle(xs)
    K = 3
    queue = xs[:K]
    heapify(queue)
    for x in xs[K:]:
        heappush(queue, x)
        heappop(queue)
    print(queue)  # => [7, 9, 8]


foo2()

bit = [0] * 1000010  # 1-origin
N = 1000


def bit_add(pos, val):
    x = pos
    while x <= N:
        bit[x] += val
        x += x & -x  # (x & -x) = rightmost 1 = block width


def bit_sum(pos):
    ret = 0
    x = pos
    while x > 0:
        ret += bit[x]
        x -= x & -x
    return ret


def bit_bisect(lower):
    "find a s.t. v1 + v2 + ... + va >= lower"
    x = 0
    k = 1 << (N.bit_length() - 1)  # largest 2^m <= N
    while k > 0:
        if (x + k <= N and bit[x + k] < lower):
            lower -= bit[x + k]
            x += k
        k //= 2
    return x + 1


bit_add(12, 1)
bit_add(34, 1)
bit_add(56, 1)
print(bit_sum(20))  # => 1
print(bit_sum(40))  # => 2
print(bit_sum(60))  # => 3
print(bit_bisect(2))  # => 34
