quantitiy,diff = map(int, input().split(" "))
 
sumTaste = 0
minusFlag = 0
subtraction = float('inf')
for i in range(quantitiy):
    tmp = diff + i
    sumTaste += tmp
    if(subtraction > abs(tmp)):
        subtraction = abs(tmp)
        if(tmp < 0):
            minusFlag = 1
        else:
            minusFlag = 0
#print(subtraction)
if(minusFlag == 0):
    print(sumTaste - subtraction)
else:
    print(sumTaste + subtraction)