# coding: utf-8
# Your code here!

number = [0,2,5,5,4,5,6,3,7,6]
INF = 10**14
n,m = map(int,input().split())
array = list(map(int,input().split()))
array.sort(reverse = True)

dp = [-INF]*(n+1)
dp[0] = 0

for i in range(n):
    for a in array:
        match = number[a]
        if i + match <= n:
            dp[i+match] = max(dp[i+match], dp[i]+1)

dd = dp[n]
ind = n
ans = ''

for _ in range(dd):
    for a in array:
        match = number[a]
        if ind - match < 0: continue
        if dp[ind] == dp[ind-match] + 1:
            ind -= match
            ans += str(a)
            break
print(ans)