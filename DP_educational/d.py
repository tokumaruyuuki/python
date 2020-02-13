n,w = map(int, input().split())
dp = [[0] * (w+1) for _ in range(n)]
ll = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(w+1):
        if ll[i][0] + j <= w:
            dp[i][ll[i][0] + j] = max(dp[i-1][j] + ll[i][1], dp[i][j])
        dp[i][j] = max(dp[i][j], dp[i-1][j])
#print(dp)
print(max(dp[n-1]))