N = int(input())
AS = [int(x) for x in input().split()]
result = 1
for x in AS:
    if x == 0:
        result = 0
        break
    if result == -1:
        continue
    result *= x
    if result > 10 ** 18:
        result = -1

print(result)
