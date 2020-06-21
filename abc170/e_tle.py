from collections import defaultdict
N, Q = [int(x) for x in input().split()]
rate = [None]  # 1-origin
k_to_ps = defaultdict(list)  # 1-origin
p_to_k = [None]
for i in range(N):
    A, B = [int(x) for x in input().split()]
    rate.append(A)
    k_to_ps[B].append(i + 1)
    p_to_k.append(B)

for i in range(Q):
    C, D = [int(x) for x in input().split()]
    frm = p_to_k[C]
    to = D
    k_to_ps[frm].remove(C)
    k_to_ps[to].append(C)

    buf = []
    for ps in k_to_ps.values():
        print(ps)
        if ps:
            buf.append(max(rate[p] for p in ps))
    print("max", buf)
    print(min(buf))
