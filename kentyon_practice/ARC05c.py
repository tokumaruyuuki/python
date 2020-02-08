# coding: utf-8
# Your code here!
import heapq

h,w = map(int, input().split())
ll = [list(input()) for _ in range(h)]

for i in range(h):
    for j in range(w):
        if ll[i][j] == 's':
            s_x, s_y = i,j
passed = [[False] * w for i in range(h)]

passed[s_x][s_y]  = True
q = [[0,s_x,s_y]]
heapq.heapify(q)
d1= [0,1,0,-1]
d2= [1,0,-1,0]
while q:
    n = heapq.heappop(q)
    times , x, y = n[0], n[1], n[2]
    for k in range(4):
        i = d1[k]
        j = d2[k]
        if not (0<= x+i <= h-1) or not(0 <= y+j <= w-1) or passed[x+i][y+j]:
            continue
        if ll[x+i][y+j] == 'g':
            print("YES")
            exit()
        if ll[x+i][y+j] == "#":
            if times == 2:
                continue
            heapq.heappush(q, [times+1, x+i, y+j])
        else:
            heapq.heappush(q, [times, x+i, y+j])
        passed[x+i][y+j] = True
print("NO")