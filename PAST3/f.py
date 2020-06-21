N = int(input())
M = []
for i in range(N):
    M.append(input())

answer = []
for i in range(N // 2):
    ok_chars = set(M[i]).intersection(M[N - 1 - i])
    if not ok_chars:
        print(-1)
        break
    answer.append(list(ok_chars)[0])
else:
    if N % 2 == 0:
        print("".join(answer) + "".join(reversed(answer)))
    else:
        print("".join(answer) + M[N//2][0] + "".join(reversed(answer)))
