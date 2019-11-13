# coding: utf-8
# Your code here!
from math import factorial
p = 10**9 + 7
def combi(a,b,p):
    return factorial(a) // (factorial(b) * factorial(a-b)) % p if(a-b>=0) else 0
def choice(a,b,p):
    return factorial(a) // (factorial(b) * factorial(a-b)) % p if (a-b>=0) else 0
balls, red = map(int,input().split(' '))

def ans(ball):
    #print(combi(balls-red+1,ball,p) ,choice(red-1,i-1,p))
    return combi(balls-red+1,ball,p) * choice(red-1,i-1,p) % p

for i in range(1,red+1):
    print(ans(i))