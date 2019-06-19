numberList = list(map(int, input().split(" ")))

ansArray = []

for i in range(3):
    for j in range(1,4):
        for k in range(2,5):
            if((numberList[i] + numberList[j] + numberList[k]) not in ansArray):
                ansArray.append(numberList[i] + numberList[j] + numberList[k])

ansArray.sort(reverse=True)
print(ansArray[2])
---------------------------------------
numberList = list(map(int, input().split(" ")))

numberList.sort()

print(max(numberList[4] + numberList[3] + numberList[0], numberList[4] + numberList[2] + numberList[1]))