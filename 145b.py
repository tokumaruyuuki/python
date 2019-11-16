# coding: utf-8
# Your code here!
 
ll=int(input())
array = list(input())
if(ll==1 or ll%2 == 1):
    print('No')
else:
    index = ll//2
    if(array[:index] == array[index:]):
        print('Yes')
    else:
        print('No')