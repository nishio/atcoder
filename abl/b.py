A, B, C, D = map(int, input().split())
# if A <= D <= B or A <= C <= B:  # NG
# if A <= D <= B or A <= C <= B or C <= A <= D:
#     print("Yes")
# else:
#     print("No")
if D < A or B < C:
    print("No")
else:
    print("Yes")
