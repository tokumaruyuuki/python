n,k = map(int, input().split())
ll = list(map(int, input().split()))
dp = [0] * n
dp[1] = abs(ll[0] - ll[1])
for i in range(2, n):
    s_ind = i - k if i - k > 0 else 0
    min_num = float('inf')
    for j in range(s_ind, i):
        min_num = min(min_num, dp[j] + abs(ll[j] - ll[i]))
    dp[i] = min_num

print(dp[n-1])