# coding: utf-8
# Your code here!
d,n = map(int, input().split())
temp = [int(input()) for _ in range(d)]
ll = [list(map(int, input().split())) for _ in range(n)]# [a,<= <= ,b , importance]
dp = [[float('-inf') for _ in range(n)] for _ in range(d)] # i日目のj番目の服を選択した場合の最大値
for i in range(n):
    if not(ll[i][0] <= temp[0] <= ll[i][1]):
        continue
    dp[0][i] = 0
for i in range(1,d):
    for j in range(n):
        if not(ll[j][0] <= temp[i] <= ll[j][1]):
            continue
        past_max = float('-inf')
        for k in range(n):
            #print(j,k)
            past_max = max(past_max, dp[i-1][k] + abs(ll[k][2] - ll[j][2]))
            #print(j,k,past_max, abs(ll[k][2] - ll[j][2]))
        dp[i][j] = past_max
#print(dp)
print(max(dp[d-1]))
            
        