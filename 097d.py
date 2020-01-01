N,M = map(int, input().split())
changes = []
array = list(map(int, input().split()))
roots = [0] * N
cnt = [1] * N
for i in range(N):
    roots[i] = i

def find_roots(n):
    root = roots[n]
    if root == n:
        return root
    elif cnt[root] == 1:
        return root
    else:
        return find_roots(root)
for i in range(M):
    s,e = map(int, input().split())
    s -= 1
    e -= 1
    sr = find_roots(s)
    er = find_roots(e)
    if cnt[s] > cnt[e]:
        roots[e] = sr
        cnt[s] += cnt[e]
        cnt[e] = 0
    else:
        roots[s] = er
        cnt[e] += cnt[s]
        cnt[s] = 0
ans = 0 
for i in range(N):
    target = array[i] - 1
    if array[i] == i + 1:
        ans += 1
        continue
    root = roots[target] 
    r = find_roots(root)
    #print(r)
    if roots[i] == r:
        ans += 1
print(roots
)
print(ans)
-------------------------------
N,M = map(int, input().split())
e = [int(x)-1 for x in input().split()]
p = [i for i in range(N)]
r = [0] * N

def find(x):
    if p[x]!=x:
        p[x] = find(p[x])
    return p[x]
    
def unite(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if r[x] < r[y]:
        p[x] = y
    else:
        p[y] = x
        if r[x] == r[y]:
            r[x] += 1


def same(x,y):
    return find(x) == find(y)

for i in range(M):
    x,y = map(int, input().split())
    unite(x-1, y-1)

c = 0
for i in range(N):
    if same(i,e[i]):
        c+=1
print(c)