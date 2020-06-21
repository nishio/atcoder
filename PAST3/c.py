A, R, N = [int(x) for x in input().split()]
x = A
LIMIT = 10 ** 9
if R == 1:
    print(A)
else:
    for i in range(N - 1):
        x *= R
        if x > LIMIT:
            print("large")
            break
    else:
        print(x)
