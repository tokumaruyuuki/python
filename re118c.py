# coding: utf-8
# Your code here!
def euclid(a,b):
    while b != 0:
        a,b = b,a%b
    return a


monsters = int(input())
array = list(map(int,input().split()))
for i in range(monsters-1):
    mod = euclid(array[i], array[i+1])
    array[i+1] = mod
print(array[-1])