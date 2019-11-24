import bisect

a,b,times = map(int,input().split())
s = [-float('inf')] + [int(input()) for _ in range(a)] + [float('inf')]
t = [-float('inf')] + [int(input()) for _ in range(b)] + [float('inf')]

for _ in range(times):
    ans = float('inf')
    position = int(input())
    sindex = bisect.bisect_left(s,position)
    tindex = bisect.bisect_left(t,position)
    for ss in [s[sindex-1], s[sindex]]:
        for tt in [t[tindex-1], t[tindex]]:
            dis1 = abs(ss-position) + abs(tt-ss)
            dis2 = abs(tt-position) + abs(tt-ss)
            ans = min(ans, dis1, dis2)
    print(ans)