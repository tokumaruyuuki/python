import math
a= int(input())
b=int(input())
c = int(input())
 
def gcd(a,b):
    while b:
        a,b = b,a%b
    return a
tmp1= max(a,b)
tmp2 = min(a,b)
gcd = gcd(tmp1,tmp2)
ans = a * b // gcd
ans2 = ans
while ans < c :
    ans += ans2
print(ans)