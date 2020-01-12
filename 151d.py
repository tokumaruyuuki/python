# coding: utf-8
# Your code here!
import queue
h,w = map(int, input().split())
array = [list(input()) for _ in range(h)]

def search(x,y):
    dd = [[float('inf')] * w for _ in range(h)]
    dd[x][y] = 0
    dis1 = [1,0,-1,0]
    dis2 = [0,1,0,-1]
    q = queue.Queue()
    q.put([x,y])
    res = 0
    while not q.empty():
        n = q.get()
        #print(n)
        for i in range(4):
            if not (0 <= (n[0] + dis1[i]) <= h-1 and 0 <= (n[1] + dis2[i]) <= w-1):
                continue
            if array[n[0] + dis1[i]][n[1] + dis2[i]] == "." and dd[n[0] + dis1[i]][n[1] + dis2[i]] == float('inf'):
                dd[n[0] + dis1[i]][n[1] + dis2[i]] = dd[n[0]][n[1]] + 1
                res = max(res,  dd[n[0] + dis1[i]][n[1] + dis2[i]])
                q.put([n[0] + dis1[i], n[1] + dis2[i]])
    return res

ans = 0 
for i in range(h):
    for j in range(w):
        if array[i][j] == ".":
            ans = max(ans, search(i,j))
print(ans)