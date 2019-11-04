legend = int(input())
mon = list(map(int,input().split(' ')))
led = list(map(int,input().split(' ')))

ans = 0
for i in range(legend):
    if(mon[i] >= led[i]):
        ans += led[i]
        continue
    else:
        led[i] -= mon[i]
        ans += mon[i]
        if(mon[i+1] >= led[i]):
            ans += led[i]
            mon[i+1] -= led[i]
        else:
            ans += mon[i+1]
            mon[i+1] = 0
print(ans)