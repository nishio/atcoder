N, X, T = map(int, input().split())

k = N // X
if N % X:
    k += 1
print(k * T)
