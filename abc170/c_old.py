X, N = [int(x) for x in input().split()]
PS = [int(x) for x in input().split()]
mindist = 1e+99
for p in PS:
    dist = abs(X - p)
    if dist < mindist:
        mindist = dist
        answer = p
    elif dist == mindist:
        if p < answer:
            ansewr = p
print(answer)
