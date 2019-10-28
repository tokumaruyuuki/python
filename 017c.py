# coding: utf-8
# Your code here!
n,m = map(int,input().split(' '))
scoreArray = [0] * (m + 1)
sumscore = 0
for _ in range(n):
    sindex,eindex,score = map(int,input().split(' '))
    scoreArray[sindex-1] += score
    scoreArray[eindex] -= score
    sumscore += score
for i in range(1,m+1):
    scoreArray[i] += scoreArray[i-1]
scoreArray.pop(-1)
diff = min(scoreArray)
print(sumscore - diff)
