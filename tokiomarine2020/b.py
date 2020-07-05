A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())
diff = abs(A - B)
dspeed = V - W
if dspeed * T >= diff:
    print("YES")
else:
    print("NO")
