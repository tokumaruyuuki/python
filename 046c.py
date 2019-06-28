import math
 
n = int(input())
a = 1
b = 1
 
for i in range(n):
    x,y = map(int, input().split(" "))
    tmp = max(math.ceil(a/x),math.ceil(b/y))
    a = tmp * x
    b = tmp * y
 
print(a+b)