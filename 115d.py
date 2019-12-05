# coding: utf-8
# Your code here!

n,m = map(int, input().split())
point = []

ans = 0
a = 1
p = 1
for i in range(n):
    a *= 2
    a += 3
    p *= 2
    p += 1
 
#print(a, p)
 
while a >= 1:
    if m == a :
        ans += p
        break
    elif (a+1)//2+1 <= m <= a-1:
        m -= 2+(a-3)//2
        ans += p//2 + 1
    elif  m == (a+1)//2:
        ans += p//2 + 1
        break
    elif 2 <= m <= (a+1)//2-1:
        m -= 1
    elif m == 1:
        break
 
    a -= 3
    a //= 2
    p -= 1
    p //= 2
 
    #print(a, p)
 
print(ans)