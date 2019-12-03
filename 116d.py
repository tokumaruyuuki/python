from heapq import heappush, heappop

n, k = map(int, input().split())
ll = [tuple(map(int, input().split())) for _ in range(n)]
ll = list(sorted(ll, key = lambda x:-x[1]))
ll_sum, ll_kind = 0,0
exist_num = [0 for _ in range(n)]
hh = []

for kk, d in ll[:k]:
    ll_sum += d
    if exist_num[kk-1] > 0:
        heappush(hh, (d,kk))
    if exist_num[kk-1] == 0:
        ll_kind += 1
    exist_num[kk-1] += 1

ans = ll_sum + ll_kind * ll_kind

for t, d  in ll[k:]:
    if len(hh) == 0:
        break
    if exist_num[t-1] > 0:
        continue
    else:
        _d,_t = heappop(hh)
        exist_num[_t-1] -= 1
        exist_num[t-1] += 1
        ll_kind += 1
        ll_sum += d - _d
        ans = max(ans, ll_sum + ll_kind*ll_kind)

print(ans)