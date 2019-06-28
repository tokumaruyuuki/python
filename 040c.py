n = int(input())
array = list(map(int, input().split(" ")))
point = [0, abs(array[0] - array[1])]
for i in range(2,n):
    tmp1 = abs(array[i] - array[i-2])
    tmp2 = abs(array[i] - array[i-1])
    if(tmp1 + point[i-2] > tmp2 + point[i-1]):
        point.append(point[i-1] + tmp2)
    else:
        point.append(point[i-2] + tmp1)



print(point[-1])