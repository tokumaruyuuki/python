n = int(input())

array = list(map(int, input().split(" ")))

colortype = [0] * 9
for i in range(n):
    if(1 <=array[i] and array[i] <= 399):
        colortype[0] = 1
    elif(400 <= array[i] and array[i] <= 799):
        colortype[1] = 1
    elif(800 <= array[i] and array[i] <= 1199):
        colortype[2] = 1
    elif(1200 <= array[i] and array[i] <= 1599):
        colortype[3] = 1
    elif(1600 <= array[i] and array[i] <= 1999):
        colortype[4] = 1
    elif(2000 <= array[i] and array[i] <= 2399):
        colortype[5] = 1
    elif(2400 <= array[i] and array[i] <= 2799):
        colortype[6] = 1
    elif(2800 <= array[i] and array[i] <= 3199):
        colortype[7] = 1
    elif(3200 <= array[i]):
        colortype[8] += 1

ans = 0

for i in range(8):
    if(colortype[i] == 1):
        ans += 1
other = colortype[8]

minans = ans
maxans = 8 if(ans + other >= 8 or ans == 8) else ans + other

print(minans, maxans)


--------------------------------------------------------

n = int(input())

array = list(map(int, input().split(" ")))

colortype = [0] * 9
for i in range(n):
    div = int(array[i] / 400)
    if(div == 0):
        colortype[0] = 1
    elif(div == 1):
        colortype[1] = 1
    elif(div == 2):
        colortype[2] = 1
    elif(div == 3):
        colortype[3] = 1
    elif(div == 4):
        colortype[4] = 1
    elif(div == 5):
        colortype[5] = 1
    elif(div == 6):
        colortype[6] = 1
    elif(div == 7):
        colortype[7] = 1
    elif(div >= 8):
        colortype[8] += 1

ans = 0

for i in range(8):
    if(colortype[i] == 1):
        ans += 1
other = colortype[8]

minans = ans if(ans != 0) else 1
maxans =ans + other

print(minans, maxans)