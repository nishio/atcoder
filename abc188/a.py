X, Y = map(int, input().split())
if X > Y:
    Y, X = X, Y
if X + 3 > Y:
    print("Yes")
else:
    print("No")
