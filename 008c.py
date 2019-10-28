n = int(input())
coins = []
for i in range(n):
    coins.append(int(input()))
ans = 0
coinsArray = [0] * n
for i in range(n):
    count = 0
    for j in range(n):
        if(i == j):continue
        if(coins[i] % coins[j] == 0):
            coinsArray[i] += 1
for cnt in coinsArray:
    ans += ((cnt // 2) + 1) / (cnt+1)
            
print(ans)