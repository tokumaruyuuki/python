n, k = map(int, input().split())
a = [int(input()) for i in range(n)]
if 0 in a:
    print(n)
    exit()
else: 
    ans = 0
    mul = 1
    right = 0
 
    for left in range(n):
        while (right < n) and (mul * a[right] <= k):
            mul *= a[right]
            right += 1
 
        ans = max(ans, right - left)
 
        if left == right:
            right += 1
        else:
            mul /= a[left]
 
    print(ans)     