# coding: utf-8
# Your code here!
n = int(input())
ll = []
for i in range(n):
    ll.append(list(map(int, input().split())))

dp = [[0] * 3 for _ in range(n)]
dp[0][0] = ll[0][0]
dp[0][1] = ll[0][1]
dp[0][2] = ll[0][2]
for i in range(1,n):
    for j in range(3):
        if j == 0:
            dp[i][j] = ll[i][j] + max(dp[i-1][1],dp[i-1][2])
        elif j == 1:
            dp[i][j] = ll[i][j] + max(dp[i-1][0],dp[i-1][2])
        elif j == 2:
            dp[i][j] = ll[i][j] + max(dp[i-1][0],dp[i-1][1])
print(max(dp[n-1]))