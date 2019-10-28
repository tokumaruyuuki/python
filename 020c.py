# coding: utf-8
# Your code here!
import heapq
ver,hor,timeLimit = map(int,input().split(' '))
dansion = [list(input()) for _ in range(ver)]
dixy = [[0,1],[1,0],[-1,0],[0,-1]]
for i,line in enumerate(dansion):
        if ('S' in line):
            sx,sy = i,line.index('S')
        if ('G' in line):
            gx,gy = i,line.index('G')

def search(m):
    movecost = [[float('inf')]*hor for _ in range(ver)] 
    canmove = [[True]*hor for _ in range(ver)]
    movecost[sx][sy] = 0
    canmove[sx][sy] = False
    hh = []
    heapq.heappush(hh,(0,sx,sy))
    while hh:
        #print(hh)
        #print('-----------')
        nn = heapq.heappop(hh)
        if(nn[0] >=timeLimit):break
        for px,py in dixy:
            nx,ny = nn[1]+px,nn[2]+py
            if(not 0<=nx<ver):continue
            if(not 0<=ny<hor):continue
            if(not canmove[nx][ny]): continue
            cost = m if dansion[nx][ny] == '#' else 1
            movecost[nx][ny] = cost + nn[0]
            if (nx == gx and ny == gy):
                return True
            if(canmove[nx][ny]):
                heapq.heappush(hh,(movecost[nx][ny],nx,ny))
            canmove[nx][ny] = False
    return False


maxtime = timeLimit
mintime = 1
while (maxtime - mintime) > 1:
    middle = (maxtime + mintime) // 2
    #print(middle)
    
    #print(maxtime,mintime)
    #print('------------------')
    if(search(middle)):
        mintime = middle
    else:
        maxtime = middle
print(maxtime-1)