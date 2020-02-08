import itertools
import queue
n, m =map(int, input().split())
ll = [[] for _ in range(n)]
for i in range(m):
    a,b = map(int, input().split())
    ll[a-1].append(b-1)
    ll[b-1].append(a-1)
cannum = []
for i in range(1,n+1):
    cannum.append(i)
ans = 0
for l in itertools.permutations(cannum):
    if l[0] != 1:
        continue
    tmp_l = []
    for i in range(len(l)-1):
        if (l[i+1]-1) not in ll[l[i]-1]:
            continue
        elif l[i]-1 in tmp_l:
            continue
        tmp_l.append(l[i]-1)
    ans += 1 if len(tmp_l) == n-1 else 0
print(ans)