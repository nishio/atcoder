from collections import defaultdict
N, Q = [int(x) for x in input().split()]
p_rate = [None]  # 1-origin
# k: kindergarden, p=person
k_to_ps = defaultdict(list)  # 1-origin
p_to_k = [None]
k_to_max = defaultdict(int)

k_to_max_p = {}
p_to_next_p = [None] * (N + 1)
p_to_prev_p = [None] * (N + 1)

for i in range(N):
    A, B = [int(x) for x in input().split()]
    p_rate.append(A)
    k_to_ps[B].append(i + 1)
    p_to_k.append(B)

for k in k_to_ps:
    ps = k_to_ps[k]
    ps.sort(key=lambda p: p_rate[p], reversed=True)
    cur = ps[0]
    k_to_max_p[k] = cur
    p_to_prev_p[cur] = None
    prev = cur
    for cur in ps[1:]:
        p_to_prev_p[cur] = prev
        p_to_next_p[prev] = cur
        prev = cur
    p_to_next_p[cur] = None

for i in range(Q):
    C, D = [int(x) for x in input().split()]
    frm = p_to_k[C]
    to = D
    k_to_ps[frm].remove(C)
    k_to_ps[to].append(C)

    buf = []
    for ps in k_to_ps.values():
        # print(ps)
        if ps:
            buf.append(max(p_rate[p] for p in ps))
    # print("max", buf)
    print(min(buf))
