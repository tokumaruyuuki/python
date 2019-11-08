# coding: utf-8
# Your code here!
import fractions
a,b,c,d = map(int,input().split(' '))
minusc = b//c - (a-1)//c
minusd = b//d - (a-1)//d
gg=max(c,d)
mm =min(c,d)
kk = gg * mm / fractions.gcd(gg, mm)
jj = b//kk - (a-1)//kk
print((b-a+1) - minusc - minusd + int(jj))