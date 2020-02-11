# coding: utf-8
# Your code here!
n = int(input())
ll = list(map(int, input().split()))
dp = [0] * n
dp[1] = abs(ll[0] - ll[1])
for i in range(2,n):
    dp[i] = min(dp[i-2] + abs(ll[i-2] - ll[i]), dp[i-1] + abs(ll[i-1] - ll[i]))
print(dp[n-1])