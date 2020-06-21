import sys
from collections import defaultdict
N, M = [int(x) for x in sys.stdin.readline().split()]
edges = defaultdict(list)
for i in range(M):
    A, B = [int(x) for x in sys.stdin.readline().split()]
    edges[A].append(B)
    edges[B].append(A)

answer = [None] * (N + 1)
visited = [1]
while True:
    new_visited = []
    for v in visited:
        for w in edges[v]:
            if answer[w] == None:
                answer[w] = v
                new_visited.append(w)
    visited = new_visited
    if not visited:
        break

answer = answer[2:]
if None in answer:
    print("No")
else:
    print("Yes")
    for a in answer:
        print(a)
