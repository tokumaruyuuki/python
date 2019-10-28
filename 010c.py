import math
startx,starty,endx,endy,perTime,perV = map(int,input().split(' '))
n = int(input())
limitTime = perTime * perV
flag = False
for i in range(n):
    pointx,pointy = map(int,input().split(' '))
    load1 = (startx - pointx)**2 + (starty - pointy)**2
    load2 = (endx - pointx)**2 + (endy - pointy)**2
    needTime = (math.sqrt(load1) + math.sqrt(load2))
    if (needTime <= limitTime):
        flag = True
        break
if (flag):
    print('YES')
else:
    print('NO')