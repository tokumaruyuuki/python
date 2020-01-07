N, C = map(int,input().split())
sushi = list(list(map(int,input().split()))for i in range(N))
r1,l1,r2,l2 = [0]*(N+1),[0]*(N+1),[0]*(N+1),[0]*(N+1)
 
eat = 0
for i in range(N):
    a,b = sushi[i]
    eat += b
    r1[i+1] = max(r1[i],eat-a)
    r2[i+1] = max(r2[i],eat-a*2)
eat = 0
for i in range(N-1,-1,-1):
    a,b = sushi[i]
    eat += b
    l1[i] = max(l1[i+1],eat-(C-a))
    l2[i] = max(l2[i+1],eat-(C-a)*2)
 
ans = 0
for i in range(N+1):
    ans = max(ans,r1[i]+l2[i],r2[i]+l1[i])
 
print(ans)