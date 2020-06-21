N = int(input())
S = [input(), input(), input(), input(), input()]

PATTERNS = """
####.##.##.####
.#.##..#..#.###
###..#####..###
###..####..####
#.##.####..#..#
####..###..####
####..####.####
###..#..#..#..#
####.#####.####
####.####..####
""".strip().split()

result = ""
for i in range(N):
    char = "".join(S[j][i * 4 + 1:i * 4 + 4] for j in range(5))
    result += str(PATTERNS.index(char))
print(result)
