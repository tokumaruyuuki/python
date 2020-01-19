from fractions import gcd
n = int(input())
array = list(map(int, input().split()))
 
def lcm(x, y):
    return (x * y) // gcd(x, y)
g = array[0]
for i in range(1,n):
    g = lcm(g,array[i])
ans = 0
for i in range(n):
    ans += g // array[i]
print(ans % (10**9+7))