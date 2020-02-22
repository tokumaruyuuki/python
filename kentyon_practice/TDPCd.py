n,d = map(int, input().split())
div = {2:0, 3:0,5:0}
def div_num(target, di):
    cnt = 0
    while target % di == 0:
        target //=di
        cnt+=1
    return (cnt, target)
div[2],di = div_num(d,2)
div[3],di = div_num(di,3)
div[5],di = div_num(di,5)
J,K,L = div[2], div[3], div[5]
if J == K == L == 0 or di != 1:
    print(0)
    exit()
dp = [[[[0 for _ in range(div[5]+1)] for _ in range(div[3]+1)] for _ in range(div[2]+1)] for _ in range(n+1)]
dp[0][0][0][0] = 1
for i in range(1,n+1):
    for j in range(J+1):
        for k in range(K+1):
            for l in range(L+1):
                if dp[i-1][j][k][l] == 0:
                    continue
                dp[i][j][k][l] += dp[i-1][j][k][l] / 6
                dp[i][min(j+1,J)][k][l] += dp[i-1][j][k][l] / 6
                dp[i][j][min(k+1,K)][l] += dp[i-1][j][k][l] / 6
                dp[i][min(j+2,J)][k][l] += dp[i-1][j][k][l] / 6
                dp[i][j][k][min(l+1,L)] += dp[i-1][j][k][l] / 6
                dp[i][min(j+1,J)][min(k+1, K)][l] += dp[i-1][j][k][l] / 6
print(dp[n][J][K][L])
