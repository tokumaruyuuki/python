import math

n = int(input())

limit = int(math.sqrt(n))

maxnum1 = 0
maxnum2 = 0
for i in range(1,limit+1):
    if(n % i == 0):
        maxnum1 = i
        maxnum2 = int(n / i)

ans = maxnum1 if(maxnum1 >= maxnum2) else maxnum2
print(len(str(ans)))