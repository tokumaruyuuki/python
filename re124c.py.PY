# coding: utf-8
# Your code here!
array = list(input())
ans = 0 
for i in range(1,len(array)):
    if(array[i-1] == array[i]):
        array[i] = '1' if(array[i-1] == '0') else '0'
        ans+=1
print(ans)
