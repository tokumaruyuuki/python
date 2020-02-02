import queue
h,w = map(int, input().split())
ll = []
for i in range(h):
    ll.append(list(input()))
passed = [[False] * w for _ in range(h)]
cnt = [[float('inf')] * w for _ in range(h)]
d1 = [1,0,-1,0]
d2 = [0,1,0,-1]
def bfs(x,y):
    q = queue.Queue()
    q.put([x,y])
    while not q.empty():
        tmp = q.get()
        a,b = tmp[0], tmp[1]
        for i in range(4):
            ta = a + d1[i]
            tb = b + d2[i]
            if 0<=ta<=h-1 and 0<=tb<=w-1 and passed[ta][tb] == False and ll[ta][tb] != "#":
                passed[ta][tb]= True
                cnt[ta][tb] = min(cnt[a][b] + 1, cnt[ta][tb])
                q.put([ta,tb])
                if ta == h-1 and tb == w-1:
                    return True
    return False
passed[0][0] = True
cnt[0][0] = 0
flag=bfs(0,0)
if flag:
    b = 0
    for i in range(h):
        for j in range(w):
            if ll[i][j] == "#":
                b += 1
    ans = h*w - (b + cnt[h-1][w-1] + 1)
else:
    ans = -1

print(ans)
                