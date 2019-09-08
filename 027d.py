# coding: utf-8
# Your code here!
array = input()
#順に[＞][＜]の個数
plus = array.count('+') 
minus = array.count('-')
sortArray = []
#print(array)
for i in range(len(array)):
    if(array[i] == '+'):
        plus -= 1
    elif(array[i] == '-'):
        minus -= 1
    else:
        sortArray.append((plus - minus))

sortArray.sort()
halfIndex = len(sortArray) // 2
#print(sortArray)
ans = (sum(sortArray[halfIndex:]) - sum(sortArray[:halfIndex]))
print(ans)