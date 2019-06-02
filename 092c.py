spot = int(input())
array = list(map(int, input().split(" ")))
sumnum = 0
for i in range(spot):
    if(i+1 > spot-1):
        sumnum += abs(array[i])
    else:
        sumnum += abs(array[i] - array[i+1])
    ##print(sumnum)
sumnum += abs(array[0])
##print(sumnum)
for i in range(spot):
    if(i == 0):
        ans = sumnum - (abs(array[i]) + (abs(array[i] - array[i+1]))) + abs(array[i+1])
    elif(i+1 >= len(array)):
        ans = sumnum - (abs(array[i-1] - array[i]) + abs(array[i])) + abs(array[i-1])
    else:
        ans = sumnum + abs(array[i-1] - array[i+1]) - (abs(array[i] - array[i+1]) + abs(array[i-1] - array[i]))
    print(ans)