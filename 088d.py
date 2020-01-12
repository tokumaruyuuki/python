import sys
import queue
sys.setrecursionlimit(3000)
h,w = map(int, input().split())
grid = [list(input()) for _ in range(h)]
pattern = [[float('inf')] * w for _ in range(h)]
black = 0
all_grid = h*w
for i in range(h):
    black += grid[i].count("#")
direction_h = [1,0,-1,0]
direction_v = [0,1,0,-1]

def bfs():
    next_q = queue.Queue()
    next_q.put([0,0])
    pattern[0][0] = 0
    while not next_q.empty():
        n = next_q.get()
        n_x, n_y = n[0],n[1]
        
        for i in range(4):
            n_xx, n_yy = n_x+direction_h[i], n_y+direction_v[i] 
            if 0 <= n_xx <= h-1 and 0 <= n_yy <= w-1 and grid[n_xx][n_yy] == ".":
                if pattern[n_xx][n_yy] > pattern[n_x][n_y] + 1:
                    pattern[n_xx][n_yy] = pattern[n_x][n_y] + 1
                    next_q.put([n_xx,n_yy])
        #print(next_q)

bfs()
if pattern[h-1][w-1] == float('inf'):
    print(-1)
else:
    print(all_grid - black - pattern[h-1][w-1] - 1)