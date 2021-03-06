MUSHI, NYUSHI = map(int, input().split())
NYUKO = MUSHI + NYUSHI
if NYUKO >= 15 and NYUSHI >= 8:
    print(1)
elif NYUKO >= 10 and NYUSHI >= 3:
    print(2)
elif NYUKO >= 3:
    print(3)
else:
    print(4)