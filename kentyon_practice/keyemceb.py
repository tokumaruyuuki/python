n = int(input())
arms = []
for i in range(n):
    a,b = map(int, input().split())
    arms.append([a+b, a-b])
arms = sorted(arms, key = lambda x : x[0])
now = arms[0][0]
ans = 1
for i in arms:
    if now <= i[1]:
        ans += 1
        now = i[0]
print(ans)