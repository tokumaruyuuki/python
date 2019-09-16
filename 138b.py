n = int(input())
array = list(map(int,input().split(' ')))
div = 0
for i in array:
    div += 1 / i
print(1/div)