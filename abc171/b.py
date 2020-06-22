N, K = map(int, input().split())
PS = list(map(int, input().split()))
PS.sort()
print(sum(PS[:K]))
