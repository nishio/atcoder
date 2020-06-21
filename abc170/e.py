from collections import defaultdict
from heapq import heappush, heappop
import sys
input = sys.stdin.buffer.readline


def update_segtree(k, v):
    pass


def main():
    global segtree_node
    N, Q = [int(x) for x in input().split()]
    # k: kindergarden, p: person
    p_to_rate = [None] * (N + 1)  # 1-origin
    p_to_k = [None] * (N + 1)  # 1-origin
    # dsc. order heapq for each k
    MAX_K = 200000
    k_to_ps = defaultdict(list)

    for i in range(N):
        A, B = [int(x) for x in input().split()]
        I = i + 1
        p_to_rate[I] = A
        p_to_k[I] = B
        heappush(k_to_ps[B], (-A, I))

    # Segment Tree
    WIDTH = 1 << MAX_K.bit_length()
    max_ps = [1e+99] * WIDTH
    segtree_node = [1e+99] * WIDTH
    for k in k_to_ps:
        neg_rate, max_p = k_to_ps[k][0]
        max_ps[k] = -neg_rate
        i = (WIDTH + k) // 2
        segtree_node[i] = min(segtree_node[i], -neg_rate)

    # for i in reversed(range(1, WIDTH // 2)):
    #     segtree_node[i] = min(
    #         segtree_node[i * 2],
    #         segtree_node[i * 2 + 1]
    #     )

    # @profile
    # def update_segtree(k, v):
    #     global segtree_node
    #     max_ps[k] = v
    #     i = (WIDTH + k) // 2
    #     segtree_node[i] = min(max_ps[k // 2 * 2], max_ps[k // 2 * 2 + 1])
    #     i //= 2
    #     while i:
    #         segtree_node[i] = min(segtree_node[i * 2], segtree_node[i * 2 + 1])
    #         i //= 2

    answers = [0] * Q
    import sys
    #CDs = sys.stdin.read().split()
    for t in range(Q):
        #C, D = [int(x) for x in input().split()]
        C, D = map(int, input().split())
        #C = int(CDs[t * 2])
        #D = int(CDs[t * 2 + 1])
        # src = p_to_k[C]
        # dst = D
        # rateC = p_to_rate[C]
        # p_to_k[C] = dst

        # # remove from `src`
        # # print(f"move {C} from {src} to {dst}")
        # neg_rate, max_p = k_to_ps[src][0]
        # if max_p == C:
        #     # print("max person leaving")
        #     heappop(k_to_ps[src])
        #     #rate, max_p = new_head = max(k_to_ps[src])
        #     if not k_to_ps[src]:
        #         # now it is empty
        #         update_segtree(src, 1e+99)
        #     else:
        #         # find next person
        #         while True:
        #             if not k_to_ps[src]:
        #                 update_segtree(src, 1e+99)
        #                 break
        #             neg_rate, max_p = k_to_ps[src][0]
        #             # print(f"next {max_p}")
        #             if p_to_k[max_p] != src:
        #                 heappop(k_to_ps[src])
        #                 continue
        #             update_segtree(src, -neg_rate)
        #             break
        # else:
        #     # not max person leaving, no update on max_ps
        #     pass

        # # move to `dst`
        # if not k_to_ps[dst]:
        #     # destination is empty
        #     heappush(k_to_ps[dst], (-rateC, C))
        #     update_segtree(dst, rateC)
        # else:
        #     # compare to existing max person
        #     neg_rate, max_p = k_to_ps[dst][0]
        #     if -neg_rate < rateC:
        #         # max person changed
        #         update_segtree(dst, rateC)
        #     else:
        #         # no update on max_ps
        #         pass
        #     heappush(k_to_ps[dst], (-rateC, C))

        # print([k_to_ps[x] for x in [1, 2, 3]])
        # print([max_ps[x] for x in [1, 2, 3]])
        # print(segtree_node[1])
        answers[t] = segtree_node[1]
    print(*answers, sep="\n")


main()
