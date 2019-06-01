dice, targetNumber = map(int, input().split(" "))

ans = 0.0

for i in range(1,dice+1):
    now = i
    tmp = 1.0 / dice
    while (now < targetNumber):
        now *= 2
        tmp *= 0.5
    ans += tmp
    ##print(tmp)

print(ans)