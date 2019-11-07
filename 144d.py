import math
 
a,b,x = map(int,input().split(' '))
yy = 2*x / (a**2) - b
if(yy>0):
    yyy = b - yy
    ans = math.degrees(math.atan(yyy/a))
else:
    yyy = ((2*x)/(a*b))
    ans = math.degrees(math.atan(b/yyy))
print(ans)