N = int(input())
AS = [int(x) for x in input().split()]

AS.sort(reverse=True)
MAX_AS = AS[0]
table = [0] * (MAX_AS + 1)  # 1..max(AS)

alreadyVisited = {}
for i in range(N):
    x = dx = AS[i]
    if alreadyVisited.get(x, False):
        table[x] = 0
        continue
    alreadyVisited[x] = True

    table[x] = 1
    while True:
        x += dx
        if x > MAX_AS:
            break
        table[x] = 0

print(sum(table))
