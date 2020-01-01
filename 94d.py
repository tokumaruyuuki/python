import math
n = int(input())
array = list(map(int ,input().split()))
array.sort(reverse=True)
ans = 0

def binary_serch(x):
    r = 0
    l = n - 1
    middle = 1
    while l - r > 1:
        middle = (r+l) // 2
        #print(array[middle], middle, x//2)
        if (x % 2 == 0 and  array[middle] == x // 2) or (x % 2 == 1 and (array[middle] == x // 2 - 1 or array[middle] == x // 2 + 1)):
            return middle
        elif array[middle] > x // 2:
            r =  middle
        else:
            l = middle
    if abs(array[r] - x // 2) < abs(array[l] - x // 2):
        return r
    else:
        return l

def comb(a,b):
    upper = math.factorial(a) // math.factorial(a-b)
    down = math.factorial(b)
    return upper // down

a = array[0]
b = array[binary_serch(a)]
print(a, b)