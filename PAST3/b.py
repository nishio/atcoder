from collections import defaultdict
N, M, Q = [int(x) for x in input().split()]
solverCount = defaultdict(int)
person = defaultdict(list)
for i in range(Q):
    f, *v = [int(x) for x in input().split()]
    if f == 2:
        player, question = v
        solverCount[question] += 1
        person[player].append(question)
    elif f == 1:
        player, = v
        score = 0
        for q in person[player]:
            score += (N - solverCount[q])
        print(score)
