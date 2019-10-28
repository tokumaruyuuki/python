# coding: utf-8
# Your code here!
tate,yoko = map(int,input().split(' '))
startx,starty = map(int,input().split(' '))
endx, endy = map(int,input().split(' '))
array = []
for i in range(tate):
    array.append(input())
moveArray = [[float('inf') for i in range(yoko)] for j in range(tate)]
moveArray[startx-1][starty-1] = 0
canMove = [[True for i in range(yoko)]for i in range(tate)]
canMove[startx-1][starty-1] = False
def search(x,y):
    #print(x,y)
    canMove[x][y] = False
    move = []
    for i in [0,1,-1]:
        for j in [1,-1,0]:
            if(i == j):continue
            xx = x+i
            yy = y+j
            if(not canMove[xx][yy]):continue
            #print(i,j,xx,yy)
            if(xx < 0 or xx >=tate or yy < 0 or yy >= yoko):continue
            if(array[xx][yy] != '#'):
                moveArray[xx][yy] = moveArray[x][y] + 1
                if(xx == endx-1 and yy == endy-1):
                    return moveArray[xx][yy]
                move.append([xx,yy])
    if(len(move) > 0):
        for aa in move:
            return search(aa[0],aa[1])
    return False
print(search(startx-1, starty-1))
print(moveArray)
--------------------------------------
# coding: utf-8
# Your code here!
import sys

sys.setrecursionlimit(10001)
from collections import deque
vertical,horizon = map(int,input().split(' '))
startx,starty = map(int,input().split(' '))
endx,endy = map(int,input().split(' '))
array = []
moveCost = [[float('inf') for i in range(horizon)] for i in range(vertical)]
moveCost[startx-1][starty-1] = 0
canmove = [[True for i in range(horizon)] for i in range(vertical)]
canmove[startx-1][starty-1] = False
directonv = [1,0,-1,0]
directonh = [0,1,0,-1]
queue = deque()
for i in range(vertical):
    array.append(input())
def dps(x,y):
    if(canmove[x][y]):
        print(x,y)
        move = []
        for i in range(4):
            ver = x + directonv[i]
            hor = y + directonh[i]
            if (ver < 0 or ver >= vertical or hor < 0 or hor >= horizon):continue
            if(array[ver][hor] == '#'):
                canmove[ver][hor] = False
                continue
            if (array[ver][hor] == '.' and canmove[ver][hor]):
                queue.append([ver,hor])
            move.append(moveCost[ver][hor])
        moveCost[x][y] = min(move) + 1
        canmove[x][y] = False
        if(x == endx-1 and y == endy-1):
            return True
        if(len(queue) == 0):
            return False
        else:
            nextindex = queue.popleft()
            dps(nextindex[0],nextindex[1])

for i in range(4):
    ver = startx-1+directonv[i]
    hor = starty-1+directonh[i]
    if(array[ver][hor] == '.' and canmove[ver][hor]):
        if(dps(ver,hor)):
            break
print(moveCost[endx-1][endy-1])
print(moveCost)
---------------------------------
# coding: utf-8
# Your code here!
import sys

sys.setrecursionlimit(10001)
from collections import deque
vertical,horizon = map(int,input().split(' '))
startx,starty = map(int,input().split(' '))
endx,endy = map(int,input().split(' '))
array = []
moveCost = [[float('inf') for i in range(horizon)] for i in range(vertical)]
moveCost[startx-1][starty-1] = 0
canmove = [[True for i in range(horizon)] for i in range(vertical)]
canmove[startx-1][starty-1] = False
directonv = [1,0,-1,0]
directonh = [0,1,0,-1]
queue = deque()
for i in range(vertical):
    array.append(input())
def dps(x,y):
        move = []
        for i in range(4):
            ver = x + directonv[i]
            hor = y + directonh[i]
            if (ver < 0 or ver >= vertical or hor < 0 or hor >= horizon):continue
            if(array[ver][hor] == '#'):
                canmove[ver][hor] = False
                continue
            if(array[ver][hor] == '.' and canmove[ver][hor]):
                canmove[ver][hor] = False
                queue.append([ver,hor])
            move.append(moveCost[ver][hor])
        moveCost[x][y] = min(move) + 1
        if(x == endx-1 and y == endy-1):
            return True
        if(len(queue) == 0):
            return False
        else:
            nextindex = queue.popleft()
            dps(nextindex[0],nextindex[1])

for i in range(4):
    ver = startx-1+directonv[i]
    hor = starty-1+directonh[i]
    if(array[ver][hor] == '.' and canmove[ver][hor]):
        if(dps(ver,hor)):
            break
print(moveCost[endx-1][endy-1])