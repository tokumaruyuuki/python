n=int(input())
array=list(map(int,input().split(' ')))
cnt = 0
for i in array:
    if(i<0):cnt+=1
if(cnt%2==0):
    ans=0
    for i in array:
        ans+=abs(i)
else:
    tmp = list(map(lambda n : abs(n),array))
    tmp.sort()
    ans = sum(tmp) - tmp[0]*2
print(ans)