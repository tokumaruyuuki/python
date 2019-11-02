n = int(input())
array = list(map(int,input().split(' ')))
array.sort()

while len(array) > 1:
    a = array.pop(0)
    b = array.pop(0)
    ab = (a+b) / 2
    array.insert(0,ab)
print(array[0])