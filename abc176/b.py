S = input().strip()
x = 0
for c in S:
    x += int(c)
if x % 9 == 0:
    print("Yes")
else:
    print("No")
