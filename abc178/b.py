A, B, C, D = map(int, input().split())
print(max(x * y for x in [A, B] for y in [C, D]))
