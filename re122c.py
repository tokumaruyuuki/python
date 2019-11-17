# coding: utf-8
# Your code here!
length, times = map(int,input().split(' '))
str_array = input()
for i in range(times):
    a,b = map(int,input().split(' '))
    print(str_array[a-1:b].count('AC'))

TLE
----------------------------
# coding: utf-8
# Your code here!
length, times = map(int,input().split(' '))
str_array = input()
count_array = [0] * length
cnt = 0
for i in range(1,length):
    if(str_array[i-1] == 'A' and str_array[i] == 'C'):
        cnt+=1
        count_array[i] = cnt
    else:
        count_array[i] = count_array[i-1]
#print(count_array)
for i in range(times):
    a,b = map(int,input().split(' '))
    print(count_array[b-1] - count_array[a-1])