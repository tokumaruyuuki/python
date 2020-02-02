from collections import deque
n,m = map(int, input().split())
ll = {}
for i in range(n):
    ll[i] = []
for i in range(m):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    a,b = min(a,b), max(a,b)
    ll[a].append(b)
cnt = 0
passed = [False] * n
for k,v in ll.items():
    if passed[k]:
        continue
    passed[k] = True
    cnt += 1
    q = deque(v)
    while q:
        l = q.popleft()
        passed[l] = True
        for vv in ll[l]:
            if passed[vv]:
                cnt -= 1
                q = deque()
                break
            q.append(vv)
            passed[vv] = True
print(cnt)
------------------------------

n,m = map(int, input().split())
ll = [[] * n for _ in range(n)]
passed = [False for _ in range(n)]
for _ in range(m):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    ll[a].append(b)
    ll[b].append(a)

def dfs(top,pre):
    global flag
    for tt in ll[top]:
        if tt != pre:
            if passed[tt]:
                flag = False
            else:
                passed[tt] = True
                dfs(tt, top)
cnt = 0
for i in range(n):
    if not passed[i]:
        passed[i] = True
        flag = True 
        dfs(i,-1)
        if flag:
            cnt += 1
print(cnt)