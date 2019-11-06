# coding: utf-8
# Your code here!

l,r = map(int,input().split(' '))
numrange = 2019
lr = (r-l)
if(lr>=2019):
    print(0)
else:
    ans = float('inf')
    for i in range(l,r+1):
        for j in range(i+1,r+1):
            ans = min(ans,((i*j)%2019))
    print(ans)