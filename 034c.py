# coding: utf-8
# Your code here!
import math
a,b = map(int,input().split(' '))
mod = 10**9 + 7

def calc(n,mod):
    x = 1
    for i in range(1,n+1):
        x *= i
        x %= mod
    return x
wh = calc(a+b-2,mod)
w = calc(a-1,mod)
h = calc(b-1,mod)
ans = (wh*pow(w,mod-2,mod)*pow(h,mod-2,mod))%mod
print(ans)