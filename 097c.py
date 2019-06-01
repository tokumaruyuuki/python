string = input()
number = int(input())
stringList = list(string)
count = 1
ans = "a"
alphalist = [chr(i) for i in range(97,97+26)]
for i in alphalist:
    for index in range(len(stringList)):
        if(i == stringList[index]):
            ans = stringList[index]
            count += 1
            index2 = index
            while(count < number):
                if(index2+1 >= len(stringList)):
                    break
                index2 += 1
                ans += stringList[index2]
                count += 1

print(ans)
--------------------------------------
string = input()
number = int(input())
stringList = list(string)

joinstrList = []

length = len(string)
for i in range(length):
    for j in range(number):
        endindex = i + j + 1
        if(endindex > length):
            endindex = length - 1
        if(len(stringList[i:endindex]) == 0):
            continue
        joinstrList.append("".join(stringList[i:endindex]))
##type(joinstrList)
##print(joinstrList)
##print(joinstrList)
uniqueList = list(set(joinstrList))
uniqueList.sort()
##print(uniqueList)
print(uniqueList[number-1])