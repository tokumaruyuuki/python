tate,yoko,candy = map(int, input().split(' '))
times = int(input())

array = [[0 for i in range(yoko)] for j in range(tate)]
ans = 0
tateArray = [0] * tate
yokoArray = [0] * yoko

for i in range(times):
    tmptate, tmpyoko = map(int,input().split(' '))
    tateArray[tmptate-1] += 1
    yokoArray[tmpyoko-1] += 1
    array[tmptate-1][tmpyoko-1] = 1
for i in range(tate):
    for j in range(yoko):
        tmp = tateArray[i] + yokoArray[j]
        if (array[i][j] == 1): tmp -= 1
        ans += 1 if tmp == candy else 0

print(ans)
TLE
==============================
# coding: utf-8
# Your code here!

tate,yoko,candy = map(int,input().split(' '))
times = int(input())

tateArray = [0] * tate
yokoArray = [0] * yoko
memo = [[0 for i in range(yoko)] for j in range(tate)]
for _ in range(times):
    ttate,tyoko = map(int,input().split(' '))
    tateArray[ttate-1] += 1
    yokoArray[tyoko-1] += 1
    memo[ttate-1][tyoko-1] = 1
tateDict = {}
yokoDict = {}
for i in range(candy+1):
    for j in range(tate):
        if (tateArray[j] == i):
            if (tateDict.get(i)):
                tateDict[i].append(j)
            else:
                tateDict[i] = [j]
    for h in range(yoko):
        if (yokoArray[h] == i):
            if (yokoDict.get(i)):
                yokoDict[i].append(h)
            else:
                yokoDict[i] = [h]
#print(tateDict,yokoDict)
#print(memo)
ans = 0
#debug = []
for cnt,indexx in tateDict.items():
    want1 = candy - cnt
    #want2 = candy - cnt - 1
    want3 = candy - cnt + 1
    for index in indexx:
        if (want1 in yokoDict):
            #print(index,yokoDict[want1])
            for index2 in yokoDict[want1]:
                #print(index2)
                if (memo[index][index2] == 0):
                    ans += 1
        #            debug.append([index,index2])
                    #print('await',index2)
        #if (want2 in yokoDict):
        #    for index2 in yokoDict[want2]:
        #        if (memo[index][index2] == 1):
        #            ans += 1
        #            debug.append([index,index2])
        #            #print(index,index2)
        if (want3 in yokoDict):
            for index2 in yokoDict[want3]:
                if (memo[index][index2] == 1):
                    ans += 1
        #            debug.append([index,index2])
print(ans)
#print(debug)
TLE
------------------------------
# coding: utf-8
# Your code here!

import collections
r,c,k = map(int,input().split(' '))
n = int(input())
R = [0] * r
C = [0] * c
candy = []
for _ in range(n):
    h,w = [int(_) for _ in input().split()]
    h -= 1
    w -= 1
    R[h] += 1
    C[w] += 1
    candy += [(h,w)]
cR = collections.Counter(R)
cC = collections.Counter(C)
ans = 0
for i in range(k+1):
    ans += cR[i] * cC[k-i]
for h,w in candy:
    ans += (R[h] + C[w] == k+1) - (R[h] + C[w] == k)
print(ans)