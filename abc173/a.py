N = int(input())
N %= 1000
if N == 0:
    print(0)
else:
    print(1000 - N)
