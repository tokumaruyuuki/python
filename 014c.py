# coding: utf-8
# Your code here!
n = int(input())

array = [0] * (10**6+2)
for i in range(n):
    a,b = map(int,input().split(' '))
    array[a] += 1
    array[b+1] -= 1
ans = 0
#print(array)
for i in range(1,10**6+1):
    array[i] += array[i-1]
print(max(array))