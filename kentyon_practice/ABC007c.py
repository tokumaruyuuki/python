import queue
h,w = map(int, input().split())
sx,sy = map(int, input().split())
sx -= 1
sy -= 1
ex, ey = map(int, input().split())
ex -= 1
ey -= 1
s1 = [1,0,-1,0]
s2 = [0,1,0,-1]
ll = []
for i in range(h):
    ll.append(list(input()))
cnt = [[0] * w for _ in range(h)]
passed = [[False] * w for _ in range(h)]

q = queue.Queue()
q.put([sx,sy])
passed[sx][sy] = True
while not q.empty():
    tmp = q.get()
    a,b = tmp[0], tmp[1]
    for i in range(4):
        ta = a + s1[i]
        tb = b + s2[i]
        if 0<=a<=h-1 and 0<=b<=w-1 and ll[ta][tb] == '.' and not passed[ta][tb]:
            cnt[ta][tb] = cnt[a][b] + 1
            q.put([ta,tb])
            passed[ta][tb] = True
            if ta == ex and tb == ey:
                break
print(cnt[ex][ey])