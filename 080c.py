store = int(input())

storeArray = []
scoreArray = []

for i in range(store):
    tmp = list(map(int, input().split(" ")))
    storeArray.append(tmp)
for i in range(store):
    tmp = list(map(int, input().split(" ")))
    scoreArray.append(tmp)
ans = -float('inf')
for i in range(1,1024):
    tmp22 = format(i, 'b')
    tmp2 = str(tmp22).zfill(10)
    tmpsummoney = 0
    for j in range(store):
        tmpsumstore = 0
        for k in range(10):
            #print(tmp2[k])
            if(storeArray[j][k] == 1 and tmp2[k] == '1'):
                tmpsumstore += 1
                #print(tmpsumstore)
        #print(tmpsumstore)
        tmpsummoney += scoreArray[j][tmpsumstore]
    if(tmpsummoney >= ans):
        ans = tmpsummoney

print(ans)
                
                
                