island = int(input())

array1 = input().split(" ")

arraymap = map(lambda x:int(x), array1)
array = list(arraymap)
ans = 0
sumnum = 0
for i in range(island):
    sumnum += array[i]

nowmember = 0
hopemember = 0
permember = int(sumnum / island)
if(sumnum % island != 0):
    print(-1)
else:
    for i in range(island):
        hopemember += permember
        nowmember += array[i]
        if(nowmember != hopemember):
            ans += 1
    
    print(ans)