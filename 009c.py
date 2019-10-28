n,k = map(int,input().split())
strlist = list(input())
originlist = strlist.copy()
def diff(a,b):
    needk = 0
    for index in range(n):
        if(a[index] != b[index]):
            needk += 1
    return needk
    
for i in range(n):
    preindex=i
    for afindex in range(i+1,n):
        if(strlist[preindex] > strlist[afindex]):
            tmplist = strlist.copy()
            tmplist[i], tmplist[afindex] = tmplist[afindex], tmplist[i]
            if(diff(tmplist,originlist) <= k):
                preindex = afindex
    strlist[i], strlist[preindex] = strlist[preindex], strlist[i]


print(''.join(strlist))