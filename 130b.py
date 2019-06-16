n, x = map(int, input().split(" "))
 
array = list(map(int, input().split(" ")))
 
ans = 1
index = 0
for i in range(n):
    if(index + array[i] <= x):
        index += array[i]
        ans += 1
    else:
        break
 
print(ans)