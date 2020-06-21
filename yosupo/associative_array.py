Q = int(input())
d = {}
for i in range(Q):
    typ, *arg = [int(x) for x in input().split()]
    if typ == 0:
        k, v = arg
        d[k] = v
    else:
        k, = arg
        print(d.get(k, 0))
