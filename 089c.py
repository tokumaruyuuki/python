import math
import copy

member = int(input())
marchArray = [[for i in range(5)] for j in range(5)]
print(marchArray)
for i in range(member):
    tmp = input()
    print(tmp)
    print(marchArray)
    if(tmp[0] == "M"):
        marchArray[0].append(tmp)
    elif(tmp[0] == "A"):
        marchArray[1].append(tmp)
    elif(tmp[0] == "R"):
        marchArray[2].append(tmp)
    elif(tmp[0] == "C"):
        marchArray[3].append(tmp)
    elif(tmp[0] == "H"):
        marchArray[4].append(tmp)

ans = 0
print(marchArray)
for i in range(5):
    if(len(marchArray[i]) == 0):
        continue
    for j in range(5):
        if(len(marchArray[j]) == 0):
            continue
        for g in range(5):
            if(len(marchArray[g]) == 0 or i == j or j == g or g == i):
                continue
        ans += len(marchArray[i]) * len(marchArray[j]) * len(marchArray[g])

print(ans)
            
            
            
            
            
 -----------------------------
 import itertools

time = int(input())

array = [0] * 5

for i in range(time):
    tmp = input()
    if(tmp[0] == "M"):
        array[0] += 1
    elif(tmp[0] == "A"):
        array[1] += 1
    elif(tmp[0] == "R"):
        array[2] += 1
    elif(tmp[0] == "C"):
        array[3] += 1
    elif(tmp[0] == "H"):
        array[4] += 1
count = 0
for i in range(5):
    if(array[i]>=1):
        count += 1
##print(array)
if(count <= 2):
    print(0)
else:
    ans = 0
    array2 = list(itertools.combinations([0,1,2,3,4], 3))
    for i in range(len(array2)):
        tmp = 1
        for j in range(3):
            if(array[array2[i][j]] == 0):
                break
            tmp *=array[array2[i][j]]
            #print(array[array2[i][j]])
            #print(tmp)
            ##print("#####")
        else:
            #print("Aaaaa")
            #print(tmp)
            ans += tmp
    print(ans)           
            
            
            
            
            
            
            
            
            
            