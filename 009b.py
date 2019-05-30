times = int(input())

array = []
for i in range(times):
    tmp = int(input())
    array.append(tmp)
array.sort(reverse=True)
maxnum = array[0]
for i in range(times):
    if(array[i] != maxnum):
        print(array[i])
        break
