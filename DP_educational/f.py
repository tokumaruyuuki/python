s = list(input())
t = list(input())
dp = [[0] * (len(t)+1) for _ in range(len(s)+1)]
ll = [[""] * (len(t)+1) for _ in range(len(s)+1)]
for i in range(len(s)):
    for j in range(len(t)):
        if s[i] == t[j]:
            dp[i+1][j+1] = max(dp[i][j] + 1, dp[i+1][j+1])
            ll[i+1][j+1] = max(ll[i][j] + s[i], ll[i+1][j+1], key = len)
        dp[i+1][j+1]= max(dp[i+1][j+1], dp[i+1][j])
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j+1])
        ll[i+1][j+1] = max(ll[i+1][j+1], ll[i+1][j], key = len)
        ll[i+1][j+1] = max(ll[i+1][j+1], ll[i][j+1], key = len)
#print(ll[len(s)],dp[len(s)])
print(ll[len(s)][len(t)])