import sys
input = sys.stdin.readline
import sys

sys.setrecursionlimit(1000000)
n,m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
passed = [[False] * m for _ in range(n)]
s_x, s_y =0,0
for i in range(n):
    for j in range(m):
        if graph[i][j] == "s":
            s_x, s_y = i, j
passed[s_x][s_y] = True
dir1 = [1,0,-1,0]
dir2 = [0,1,0,-1]
def dfs(x,y):
    for i in range(4):
        n_x, n_y = x+dir1[i], y+dir2[i]
        if not 0 <= n_x <= n-1 or not 0 <= n_y <= m-1:
            continue
        if graph[n_x][n_y] == "." and not passed[n_x][n_y]:
            passed[n_x][n_y] = True
            dfs(n_x,n_y)
        elif graph[n_x][n_y] == "g":
            print("Yes")
            exit()
dfs(s_x,s_y)
print("No")

--------
# coding: utf-8
# Your code here!
from collections import deque
h,w = map(int, input().split())
ll = []
passed = [[False]*w for _ in range(h)]
d1 = [0,1,0,-1]
d2 = [1,0,-1,0]
for i in range(h):
    ll.append(list(input()))
s_x, s_y = 0,0
for i in range(h):
    for j in range(w):
        if ll[i][j] == 's':
            s_x,s_y = i,j
            passed[i][j] = True
q = deque()
q.append([s_x,s_y])
while q:
    qq = q.popleft()
    a,b = qq[0], qq[1]
    for i in range(4):
        ta = a + d1[i]
        tb = b + d2[i]
        if not (0<=ta<=h-1) or not (0<=tb<=w-1) or ll[ta][tb] == "#" or passed[ta][tb]:
            continue
        if ll[ta][tb] == "g":
            print("Yes")
            exit()
        passed[ta][tb] = True
        q.append([ta,tb])
print("No")