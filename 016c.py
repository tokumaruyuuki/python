# coding: utf-8
# Your code here!

n,m = map(int,input().split(' '))
frindsList = [0] * n
frindsTiedList = [[] for i in range(n)]
 
for i in range(m):
    a,b = map(int,input().split(' '))
    frindsList[a-1] += 1
    frindsList[b-1] += 1
    frindsTiedList[a-1].append(b-1)
    frindsTiedList[b-1].append(a-1)

for i in range(n):
    friends = frindsTiedList[i]
    wnatnum = []
    for jj in friends:
        for jjj in frindsTiedList[jj]:
            if(jjj == i or jjj in wnatnum or jjj in friends):continue
            wnatnum.append(jjj)
    print(len(wnatnum))