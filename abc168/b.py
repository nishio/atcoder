import sys
K = int(sys.stdin.readline())
# S = sys.stdin.readline()
S = sys.stdin.readline().rstrip()
if len(S) > K:
    print(S[:K] + "...")
else:
    print(S)
