import re
S = input()


def tri(x):
    return x * (x + 1) // 2


ret = 0
print(sum(tri(len(s) // 2) for s in re.findall("(?:25)+", S)))
