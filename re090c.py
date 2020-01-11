n,m = map(int, input().split())
if n == 1 or m == 1:
    ans = max(n,m) - 2
    ans = 0 if ans < 0 else ans
    if n == m == 1:
        ans = 1
    print(ans)
else:
    ans=(n-2) * (m -2)
    ans = 0 if ans < 0 else ans
    print(ans)