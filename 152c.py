n = int(input())
array = list(map(int, input().split()))
ans = 0
m = float("inf")
for i in range(n):
    if m >= array[i]:
        m = array[i]
        ans += 1
print(ans)