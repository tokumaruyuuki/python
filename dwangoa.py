n = int(input())
a = []
for i in range(n):
    s,t = input().split()
    a.append((s,int(t)))
ans = 0
x = input()
flag = False
for i in range(n):
    if flag:
        ans += a[i][1]
    if a[i][0] == x:
        flag = True
print(ans)