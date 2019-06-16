length, sumlimit = map(int, input().split(" "))
 
array = list(map(int, input().split(" ")))
 
tmpsum = 0
ans = 0
firstIndex = 0
for i in range(length):
    tmpsum += array[i]
    #print(tmpsum >= sumlimit)
    if(tmpsum >= sumlimit):
        while tmpsum >= sumlimit:
            #print(length - (i + 1))
            ans += (length - (i))
            tmpsum -= array[firstIndex]
            firstIndex += 1
            #print(firstIndex)
 
print(ans)