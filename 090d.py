N,K = map(int, input().split())

ans = 0 

for b in range(1,N+1):
    x = N//b
    r = N - (b * x)
    #print(x, r, b)
    if b <= K:
        continue
    else:
        ans += (b - K) * x
        ans += r - K + 1 if r - K + 1> 0 else 0
    #print('pass')
if K == 0:
    ans -= N
print(ans)