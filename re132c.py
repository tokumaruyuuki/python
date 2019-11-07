# coding: utf-8
# Your code here!

n=int(input())
array=list(map(int,input().split(' ')))
array.sort()

print(array[(n//2)]-array[(n//2)-1])