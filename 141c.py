# coding: utf-8
# Your code here!

people,points,times = map(int,input().split(' '))

array  = [0] * people

for i in range(times):
    tmp = int(input())
    array[tmp-1] += 1
ans = 0
for i in array:
    if(times - i < points):
        print('Yes')
    else:
        print('No')