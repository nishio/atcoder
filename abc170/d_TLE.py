N = int(input())
AS = [int(x) for x in input().split()]

ok = []
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if AS[i] % AS[j] == 0:
            break
    else:
        ok.append(i)

print(len(ok))
