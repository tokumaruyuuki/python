# coding: utf-8
# Your code here!
import sys

sys.setrecursionlimit(2000)
n=int(input())
trees = [[] for _ in range(n)]
passed = [False] * n
ans = [None] * n
for i in range(n-1):
    t,tt,v = map(int,input().split(' '))
    trees[t-1].append([tt-1, v])
    trees[tt-1].append([t-1, v])
ans[0] = 0
passed[0] = True
def checknode(index,value,pre):
    passed[index] = True
    if(value % 2 == 0):
        ans[index] = 0 if(pre==0) else 1
    else:
        ans[index] = 1 if(pre==0) else 0
    nextlist = trees[index]
    for i,v in nextlist:
        if(passed[i]):continue
        passed[i] = True
        checknode(i,v,ans[index])
for i,v in trees[0]:
    if(passed[i]):continue
    passed[i] = True
    checknode(i,v,0)
for i in ans:
    print(i)


RecursionError
------------------------------
N = int(input())
G = [[] for i in range(N)]
 
for i in range(N-1):
    u,v,w = map(int,input().split())
    w = w%2
    G[u-1].append((v,w))
    G[v-1].append((u,w))
ans = [ -1 for i in range(N)]
ans[0] = 0
stack = [1]
 
while len(stack) > 0:
    x = stack.pop()
    p = ans[x-1]
    g = len(G[x-1])
    for i in range(g):
        y = G[x-1][i][0]
        z = G[x-1][i][1]
        a = ans[y-1]
        if a == -1:
            stack.append(y)
            if z == 0:
                ans[y-1] = p
            else:
                ans[y-1] = 1-p
for i in range(N):
    print(ans[i])