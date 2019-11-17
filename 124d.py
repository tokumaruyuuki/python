# coding: utf-8
# Your code here!
import itertools
length, times = map(int,input().split(' '))
array = list(map(int,list(input())))

legstand = []
handstand = []
cnt=1
pre=array[0]
if(array[0]==0):
    handstand.append(0)
for i in range(1,length):
    if(pre==array[i]):
        cnt+=1
    else:
        if(pre==1):
            handstand.append(cnt)
        else:
            legstand.append(cnt)
        cnt=1
        pre=array[i]
if(cnt>0):
    if(pre==0):
        legstand.append(cnt)
    else:
        handstand.append(cnt)
if(array[-1] == 0):
    handstand.append(0)
countArray=zip(handstand,legstand)
countArray=list(itertools.chain.from_iterable(list(countArray)))
countArray.append(handstand[-1])

#print(countArray)


left=0
right=0
ans=0
addRange = 2*times+1
tmp=0
for i in range(0,len(countArray),2):
    nextLeft = i
    nextRight = min(i+addRange,len(countArray))
    while(nextLeft>left):
        tmp-=countArray[left]
        left+=1
    while(nextRight>right):
        tmp+=countArray[right]
        right+=1
    ans=max(ans,tmp)
print(ans)
    
    
    
    
    
    