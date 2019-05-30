times = int(input())
 
array = [0,0,1]
if(times >= 3):
    for i in range(3,times):
        array.append((array[i-3] + array[i-2] + array[i-1]) % 10007)
    print(array[-1])
elif (times == 3):
    print(1)
else:
    print(0)