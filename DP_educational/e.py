n,w = map(int, input().split())
max_v = (10**3) * n
ll = [list(map(int, input().split())) for _ in range(n)]
dp = [[float('inf')] * (max_v+1) for _ in range(n+1)]
dp[0][0] = 0
for i in range(n):
    for j in range(max_v+1):
        if j - ll[i][1] >= 0:
            dp[i+1][j] = min(dp[i+1][j], dp[i][j- ll[i][1]] + ll[i][0])
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
ans = 0
for i in range(max_v+1):
    if dp[n][i] <= w:
        ans = i
print(ans)