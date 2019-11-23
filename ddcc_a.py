# coding: utf-8
# Your code here!
a,b = map(int,input().split())
ans = 0
if(a==b==1):
    print(1000000)
else:
    ans += 100000 if(a==3) else 0
    ans += 200000 if(a==2) else 0
    ans += 300000 if(a==1) else 0
    ans += 100000 if(b==3) else 0
    ans += 200000 if(b==2) else 0
    ans += 300000 if(b==1) else 0
    print(ans)