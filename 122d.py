#A=0 G=1 C=2 T=3 に置き換えて考える
n=int(input())
mod = 10**9+7
dp = [[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(n-2)]
for i in range(4):
    for j in range(4):
        for l in range(4):
            dp[0][i][j][l] = 1
dp[0][0][2][1] = 0 #ACG
dp[0][0][1][2] = 0 #AGC
dp[0][2][0][1] = 0 #CAG
#print(dp[0][0][0][0])
for i in range(n-3):
    for j in range(4):
        for l in range(4):
            for k in range(4):
                for m in range(4):
                    #print(dp[i + 1][k][l][m], dp[i][j][k][l])
                    dp[i + 1][k][l][m] += dp[i][j][k][l]
                    dp[i + 1][k][l][m] %= mod
                    if j == 0 and k == 2 and m == 1:
                        dp[i + 1][k][l][m] = 0
                    elif j == 0 and l == 2 and m == 1:
                        dp[i + 1][k][l][m] = 0
                dp[i + 1][0][2][1] = 0
                dp[i + 1][0][1][2] = 0
                dp[i + 1][2][0][1] = 0

print(sum(sum(sum(dp[n - 3], []), [])) % mod)