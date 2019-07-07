N, A = map(int, input().split())
x = list(map(int, input().split()))
 
X = max(x)
if X < A:
    X = A
    
y = []
for i in x:
    y += [i-A]
 
dp = [[-1] * (2*N*X+1) for _ in range(N+1)]
 
def check(j, t):
    if dp[j][t] != -1:
        return dp[j][t]
    if  j == 0 and t == N * X:
        dp[j][t] = 1
        return 1
    if j >= 1 and (t-y[j-1] < 0 or t-y[j-1] > 2 * N * X):
        dp[j][t] = check(j-1, t)
        return dp[j][t]
    if j >= 1 and 0 <= t-y[j-1] and t-y[j-1] <= 2*N*X:
        dp[j][t] = check(j-1, t) + check(j-1, t- y[j-1])
        return dp[j][t]
    dp[j][t] = 0
    return 0
 
print (check(N, N*X)-1)