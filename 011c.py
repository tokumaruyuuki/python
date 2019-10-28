n = int(input())
ng = []
for i in range(3):
    ng.append(int(input()))
dp = [float('inf')] * (n+1)
dp[n] = 0
for i in reversed(range(n+1)):
    if (i in ng): continue
    for j in [1,2,3]:
        if (i+j > n): continue
        dp[i] = min(dp[i+j] + 1,dp[i])

if (dp[0] > 100):
    print('NO')
else:
    if (n in ng):
        print('NO')
    else:
        print('YES')