water1, water2, sugar1, sugar2, sugarPerWater, limit = map(int, input().split(" "))

maxper = 0
ans = [0,0]
for i in range(limit//water1*100+1):
    left1 = limit - i * 100 * water1
    for j in range(left1//water2*100+1):
        left2 = left1 - j * 100 * water2
        for k in range(left2//sugar1+1):
            left3 = left2 - k * sugar1
            for h in range(left3//sugar2+1):
                if(i+j != 0 and k+h != 0):
                    if((k*sugar1 + h * sugar2)/(i*water1 * 100 + j * water2 * 100) > maxper and (k*sugar1 + h * sugar2)/(i*water1 + j * water2) <= sugarPerWater):
                        maxper = (k*sugar1 + h * sugar2)/(i*water1 * 100 + j * water2 * 100)
                        ans = [(k*sugar1 + h * sugar2) + (i*water1 * 100 + j * water2 * 100), (k*sugar1 + h * sugar2)]
if(maxper == 0):
    print(*(water1*100,0))
else:
    print(*ans)