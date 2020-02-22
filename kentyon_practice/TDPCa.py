# coding: utf-8
# Your code here!

n = int(input())
ll = list(map(int, input().split()))
dp = [[False] * 10001 for _ in range(101)]
dp[0][0] = True
for i in range(1,n+1):
    for j in range(10001):
        if dp[i-1][j-ll[i-1]] and j - ll[i-1] >= 0:
            dp[i][j] = True
        if dp[i-1][j]:
            dp[i][j] = True
print(dp[n].count(True))