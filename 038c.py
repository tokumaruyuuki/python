n = int(input())

array = list(map(int, input().split(" ")))

ans = n
tmp = 10**6
renzoku = 0
for i in range(n):
    if(array[i] < tmp):
        tmp = array[i]
        if(renzoku > 0):
            while renzoku > 0:
                ans += renzoku
                renzoku -= 1
    elif(array[i] > tmp):
        renzoku += 1
        tmp = array[i]
if(renzoku > 0):
    while renzoku > 0:
        ans += renzoku
        renzoku -= 1
print(ans)