# coding: utf-8
# Your code here!

n,k=map(int,input().split(' '))
ans = 0
for i in range(1,n+1):
    cnt = 0
    num = i
    while num<k:
        num*=2
        cnt+=1
    ans += (1/n) * (1 / (2**cnt))
print(ans)