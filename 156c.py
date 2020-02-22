n = int(input())
ll = list(map(int, input().split()))
ans = float("inf")
for i in range(101):
    tmp = 0
    for j in range(n):
        tmp += abs(i - ll[j])**2
    ans = min(ans, tmp)
print(ans)