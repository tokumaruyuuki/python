times = int(input())

array = input().split(" ")
ans = 0
for i in range(times):
    while (int(array[i]) % 3 == 2 or int(array[i]) % 2 == 0):
        num = int(array[i])
        array[i] = num -1
        ans += 1
    
print(ans)