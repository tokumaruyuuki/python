# coding: utf-8
# Your code here!
n = int(input())
array = list(map(int, input().split(' ')))
ans = 0
start = 0
flag = 0
number = array[0]
for i in range(1, len(array)):
    if(array[i-1] >= array[i] and flag == 0):
        flag = 1
        start = i - 1
    elif(array[i-1] < array[i] and flag == 1):
        flag = 0
        tmp = (i-1)  - start
        ans = max(ans,tmp)
if(flag == 1):
    ans = max(ans,len(array) - start - 1)
print(ans)