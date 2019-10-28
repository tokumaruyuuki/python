# coding: utf-8
# Your code here!

import itertools

n,k = map(int,input().split(' '))
array = [list(map(int,input().split())) for _ in range(n)]

for ansPattern in list(itertools.product(list(range(k)), repeat = n)):
    for index in range(n):
        if index == 0:
            tmp = array[index][ansPattern[index]]
        else:
            tmp = tmp ^ array[index][ansPattern[index]]
    if tmp == 0:
        print('Found')
        exit()
print('Nothing')