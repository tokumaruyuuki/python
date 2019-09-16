n = int(input())
maxnum = -1
second = -1
array = []
for i in range(n):
    tmp = int(input())
    if(maxnum < tmp):
        second = maxnum
        maxnum = tmp
    elif(second < tmp):
        second = tmp
    array.append(tmp)
if(array.count(maxnum) >= 2):
    for i in range(n):
        print(maxnum)
else:
    for i in array:
        if(i == maxnum):
            print(second)
        else:
            print(maxnum)