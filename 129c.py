a,b = map(int, input().split(" "))
 
array = [0] * a
 
for i in range(b):
    tmp = int(input())
    array[tmp-1] = -1
    
flag = 0
for i in range(a):
    if(i == 0):
        if(array[i] != -1):
            array[i] += 1
    elif (i == 1):
        if(array[i] != -1):
            if(array[0] == -1):
                array[1] = 1
            else:
                array[1] = 2
    elif(array[i] == -1):
        continue
    else:
        if(array[i-2] < 0 and array[i-1] < 0):
            flag = -1
            break;
        elif(array[i-2] < 0):
            array[i] = array[i-1]
        elif(array[i-1] < 0):
            array[i] = array[i-2]
        else:
            array[i] = array[i-2] + array[i-1]
if(flag == -1):
    print(0)
else:
    print(array[a-1] % 1000000007)