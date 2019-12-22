S = list(input())
MOD = 10**9+7
dp = [[0 for _ in range(4)] for _ in range(len(S)+1)]
#print(dp)
dp[0][0] = 1
for i in range(len(S)):
    s = S[i]
    for j in range(4):
        if s=='?':
            dp[i+1][j] += dp[i][j] * 3
            dp[i+1][j] %= MOD
        else:
            dp[i+1][j] += dp[i][j]
            dp[i+1][j] %= MOD
        if j < 3:
            if s == '?' or s == 'A' and j == 0 \
                        or s == 'B' and j == 1 \
                        or s == 'C' and j == 2:
                dp[i+1][j+1] += dp[i][j]
                dp[i+1][j+1] %= MOD
print(dp[len(S)][3])
    