# coding: utf-8
# Your code here!
n,w = map(int ,input().split())
dp = [[0] * (w+1)  for _ in range(n)]
ll = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(w+1):
        tmp_w = ll[i][1] + j
        if tmp_w <= w:
            dp[i][tmp_w] = max(dp[i][tmp_w], dp[i-1][j] + ll[i][0])
        dp[i][j] = max(dp[i][j], dp[i-1][j])
print(max(dp[n-1]))