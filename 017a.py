ans = 0
for i in range(3):
  a,b = map(int,input().split(' '))
  ans += int((a/10) * b)
print(ans)