movie, limit = map(int, input().split(" "))

array = list(map(int, input().split(" ")))

array.sort(reverse= True)
ans = 0
for i in range(limit)[::-1]:
    #print(i)
    tmp = (ans + array[i]) / 2
    ans = tmp
    
print(ans)