from sys import stdin
N,M = [int(x) for x in stdin.readline().rstrip().split()]
data = []
for _ in range(M):
    a,b = [int(x) for x in stdin.readline().rstrip().split()]
    data.append((a,b))
par = [i for i in range(N+1)]
rank = [0] * (N+1)
size = [1] * (N+1)
 
def find(x):
    if par[x] == x:
        return par[x]
    else:
        par[x] = find(par[x])
        return par[x]
 
def union(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if rank[x] < rank[y]:
        par[x] = y
        size[y] += size[x]
        size[x] = 0
        
    else:
        par[y] = x
        size[x] += size[y]
        size[y] = 0
        if rank[x] == rank[y]:
            rank[x] += 1
 
def check_same(x,y):
    return find(x) == find(y)
 
def check_size(x):
    return size[find(x)]
 
score = (N*(N-1))//2
ans = []
 
while data:
    ans.append(score)
    x,y = data.pop()
    a = find(x)
    b = find(y)
    if not check_same(a,b):
        score -= (check_size(x)*check_size(y))
    union(x,y)
print(*ans[::-1],sep="\n")