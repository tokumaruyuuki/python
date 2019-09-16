a,b =map(int,input().split(' '))
ans = b//a +1 if b%a !=0 else b//a
print(ans)