ans = 0
n = int(input())
for i in range(n):
  ans += (i+1) * 10000 / n
print(int(ans))