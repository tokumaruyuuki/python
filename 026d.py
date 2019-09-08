# coding: utf-8
# Your code here!
#二分探索で求めていく
import math

a,b,c = map(int, input().split(' '))

high = 2*10**3
low = 0
p = math.pi
flag = 0

ans = 0
nowHight = 0
def highnum(a,b,c,t):
    global flag
    p = math.pi
    tmp = a*t + b*math.sin(c*t*p)
    if(abs(tmp - 100) < 10**-6):
        flag = 1
        return
    else:
        return tmp 

while nowHight != 100:
    middle = (high + low) / 2
    h = highnum(a,b,c,middle)
    if(flag == 1):
        ans = middle
        break
    elif(h < 100):
        low = middle
    elif(h > 100):
        high = middle

print(ans)