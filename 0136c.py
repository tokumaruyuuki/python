n = int(input())
array = list(map(int,input().split(' ')))

for i in list(reversed(range(1,n))):
    if(array[i-1] - array[i] > 0):
        array[i-1] -= 1
    if(array[i-1] > array[i]):
        print('No')
        break
else:
    print('Yes')