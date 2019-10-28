# coding: utf-8
# Your code here!
n = int(input())
students = list(map(int,input().split(' ')))
ansList = [0] * n
for i,v in enumerate(students):
    ansList[v-1] = str(i+1)
print(' '.join(ansList))