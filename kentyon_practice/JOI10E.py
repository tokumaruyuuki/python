import queue
import sys
input = sys.stdin.readline

sys.setrecursionlimit(30000)
h,w,n = map(int, input().split())
ll = []
d1 = [1,0,-1,0]
d2 = [0,1,0,-1]
for i in range(h):
    ll.append(list(input()))
for i in range(h):
    for j in range(w):
        if ll[i][j] == 'S':
            sx,sy = i,j
            break

def bfs(x,y,target):
    pattern = [[None] * w for i in range(h)]
    q = queue.Queue()
    q.put([x,y])
    pattern[x][y] = 0
    while not q.empty():
        tmp = q.get()
        a,b= tmp[0], tmp[1]
        for i in range(4):
            ta = d1[i] + a
            tb = d2[i] + b
            if 0<=ta<=h-1 and 0<=tb<=w-1 and pattern[ta][tb] == None and ll[ta][tb] != "X":
                pattern[ta][tb] = pattern[a][b] + 1
                q.put([ta,tb])
                if ll[ta][tb] == str(target):
                    return [pattern[a][b] + 1,ta,tb]

tmp = bfs(sx,sy,1)
cnt,x,y = tmp[0], tmp[1], tmp[2]
for i in range(2,n+1):
    tmp = bfs(x,y,i)
    cnt += tmp[0]
    x,y = tmp[1], tmp[2]
print(cnt)