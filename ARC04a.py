n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(n):
        if i == j :
            continue
        ans = max(ans, ((abs(p[i][0] - p[j][0]))**2 + (abs(p[i][1] - p[j][1]))**2)**0.5)
print(ans)