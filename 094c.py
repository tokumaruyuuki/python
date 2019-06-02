number = int(input())
originlist = list(map(int, input().split(" ")))
subList = []
for i in originlist:
    subList.append(i)
subList.sort()
for i in range(number):
    subList.remove(originlist[i])
    print(subList[int(number/2) - 1])
    subList.append(originlist[i])
    subList.sort()

------------------------------------------------
length = int(input())

array = list(map(int, input().split(" ")))
centerIndex = int((length-1)/2)
##print(centerIndex)
##print(length)
for i in range(length):
    tmparray1 = array[0:i]
    tmparray2 = array[i+1:length]
    sortArray = tmparray1 + tmparray2
    sortArray.sort()
    print(sortArray[centerIndex])
---------------------------------------------------

# coding: utf-8
# Your code here!

length = int(input())

array = list(map(int, input().split(" ")))
sortArray = sorted(array)
centerIndex = int((length-1)/2)
##print(centerIndex)
##print(length)
for i in range(length):
    removeNum = array[i]
    index = sortArray.index(removeNum)
    sortArray.remove(removeNum)
    print(sortArray[centerIndex])
    sortArray.insert(index, removeNum)

    ---------------------------------------------------

length = int(input())

array = list(map(int, input().split(" ")))
sortArray = sorted(array)
centerIndex = int((length)/2) - 1
##print(centerIndex)
##print(length)
#print(sortArray)
for i in range(length):
    num = array[i]
    if(sortArray[centerIndex] > num):
        print(sortArray[centerIndex + 1])
    elif(sortArray[centerIndex] == num):
        print(sortArray[centerIndex + 1])
    else:
        print(sortArray[centerIndex])