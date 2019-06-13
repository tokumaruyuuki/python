n = int(input())

array = list(map(int, input().split(" ")))

ans1 = 0 # plus
ans2 = 0 # minus

tmpsum = 0
for i in range(n):
    if(i == 0):
        if(array[i] > 0):
            tmpsum += array[i]
        elif(array[i] == 0):
            tmpsum = 1
            ans1 += 1
        else:
            tmpsum = 1
            ans1 += -1*array[i] + 1
    else:
        if((tmpsum + array[i]) * tmpsum > 0 ):
            if(tmpsum > 0):
                ans1 += abs(-1 - (tmpsum + array[i]) )
                tmpsum = -1
            else:
                ans1 += abs(1 - (tmpsum + array[i]) )
                tmpsum = 1
        elif(tmpsum + array[i] == 0):
            if(tmpsum > 0):
                ans1 += 1
                tmpsum = -1
            else:
                ans1 += 1
                tmpsum = -1
        else:
            tmpsum += array[i]

tmpsum = 0
for i in range(n):
    if(i == 0):
        if(array[i] < 0):
            tmpsum += array[i]
        elif(array[i] == 0):
            tmpsum = -1
            ans2 += 1
        else:
            tmpsum = -1
            ans2 += array[i] + 1
    else:
        if((tmpsum + array[i]) * tmpsum > 0 ):
            if(tmpsum > 0):
                ans2 += abs(-1 - (tmpsum + array[i]) )
                tmpsum = -1
            else:
                ans2 += abs(1 - (tmpsum + array[i]) )
                tmpsum = 1
        elif(tmpsum + array[i] == 0):
            if(tmpsum > 0):
                ans2 += 1
                tmpsum = -1
            else:
                ans2 += 1
                tmpsum = -1
        else:
            tmpsum += array[i]
            
ans = ans1 if (ans1 <= ans2) else ans2

print(ans)
            
            