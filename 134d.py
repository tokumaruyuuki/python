n=int(input())
array = list(map(int,input().split(' ')))
cnt = [0]*(n+1)
ballCount = 0
ans = []

for i in range(n-1,-1,-1):
    if(sum(cnt[::i+1][1:]) % 2 != array[i]):
        ballCount+=1
        ans.append(i+1)
        cnt[i+1]+=1
print(ballCount)
if(ballCount>0):
    print(*ans)