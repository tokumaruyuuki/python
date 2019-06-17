osero, times = map(int, input().split(" "))

array = [0] * osero

for i in range(times):
    a,b = map(int, input().split(" "))
    array[a-1] += 1
    if(b != osero):
        array[b] -= 1
ans = 0
tmp = 0
for i in range(osero):
    tmp += array[i]
    if(tmp % 2 == 0):
        print(0, end = "")
    else:
        print(1, end = "")
print()