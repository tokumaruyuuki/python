from collections import deque
top, times = map(int,input().split(' '))
points = [0] * top
directions = [[] for _ in range(top)]
canmove = [True] * top
#print(directions)
for i in range(top-1):
    a,b = map(int,input().split(' '))
    directions[a-1].append(b-1)
    directions[b-1].append(a-1)
for i in range(times):
    c,d = map(int,input().split(' '))
    points[c-1] += d

que = deque([[0,points[0]]]) #[頂点、ポイント]
canmove[0] = False
#print(que)
while len(que) > 0:
    nextdic = que.popleft()
    #print(nextdic)
    points[nextdic[0]] = nextdic[1]
    if(len(directions[nextdic[0]]) != 0):
        for i in directions[nextdic[0]]:
            if(canmove[i]):
                canmove[i] = False
                que.append([i,points[i] + nextdic[1]])
ans = list(map(str, points))
print(' '.join(ans))