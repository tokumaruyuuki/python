n,k,m = map(int, input().split())
array = list(map(int, input().split()))
s = sum(array)
if m*n - s <=k:
    ans = m*n - s if m*n -s > 0 else 0
    print(ans)
else:
    print(-1)