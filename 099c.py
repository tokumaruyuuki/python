import math

money = int(input())

ans = money
for i in range(0,money+1):
    sixRange = i
    tmp = 0
    while(sixRange > 0):
        tmp += sixRange % 6
        sixRange = math.floor(sixRange / 6)
    nineRange = money - i
    while(nineRange > 0):
        tmp += nineRange % 9
        nineRange = math.floor(nineRange / 9)
    if(ans >= tmp):
        ans = tmp

print(ans)