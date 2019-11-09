steps, nosteps = map(int,input().split(' '))
nostepsArray = [False] *steps
for i in range(nosteps):
    nostepsArray[int(input())-1] = True
    
dp = [0 for _ in range(steps)]
if(not nostepsArray[0]):
    dp[0] = 1
if(len(nostepsArray)>=2 and not nostepsArray[1]):
    dp[1] = dp[0] + 1
for i in range(2,steps):
    if(nostepsArray[i]):
        continue
    dp[i] += (dp[i-1]+dp[i-2]) % (10**9+7)
    if(dp[i]==0):
        print(0)
        exit()
print(dp[-1])