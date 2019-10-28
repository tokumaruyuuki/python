# coding: utf-8
# Your code here!

n = int(input())
array = list(map(int,input().split(' ')))
for i in range(n):
    while array[i]%2 == 0:
        array[i] //= 2
print(len(set(array)))