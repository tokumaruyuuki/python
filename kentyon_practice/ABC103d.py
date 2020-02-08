n, m = map(int, input().split())
ll = []
for i in range(m):
    a,b = map(int, input().split())
    ll.append([a,b])
ll = sorted(ll , key = lambda x : x[1])
ans = 1 
now = ll[0][1]-1
for i in ll[1:]:
    if now < i[0]:
        now = i[1]-1
        ans += 1
print(ans)