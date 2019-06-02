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
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            