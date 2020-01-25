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