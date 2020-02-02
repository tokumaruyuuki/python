from collections import deque
ss = [0,1,0,-1]
dd = [1,0,-1,0]
while True:
    w,h = map(int ,input().split())
    if w == h == 0:
        break
    ll = []
    for i in range(h):
        ll.append(list(map(int, input().split())))
    cnt = 0
    passed = [[False]*w for i in range(h)]
    q = deque()
    for i in range(h):
        for j in range(w):
            if passed[i][j]:
                continue
            if ll[i][j] == 1:
                passed[i][j] = True
                q.append([i,j])
                cnt += 1
                while q:
                    l = q.popleft()
                    a,b = l[0], l[1]
                    for s in ss:
                        for d in dd:
                            if s == d == 0:
                                continue
                            ta = a + s
                            tb = b + d
                            if 0 <= ta <= h-1 and 0 <= tb <= w-1 and ll[ta][tb] == 1 and not passed[ta][tb]:
                                passed[ta][tb] = True
                                q.append([ta,tb])
    print(cnt)