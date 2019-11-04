# coding: utf-8
# Your code here!
people, times = map(int,input().split(' '))
array = list(input())
ans = 0
changeflag = False
index= 0
for i in range(1,people):
    if(array[i-1] == array[i]):
        ans+= 1
#print(ans)
for i in range(1,people):
    if(times == 0):break
    if(array[i-1] != array[i]):
        if(changeflag):
            for j in range(index,i):
                array[j] = array[index-1]
            changeflag = False
            ans += 2
            times-=1
        else:
            changeflag = True
            index = i
if(changeflag):
    ans += 1
print(ans)