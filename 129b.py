n = int(input())
array = list(map(int, input().split(" ")))
 
sumnum1 = sum(array)
sumnum2 = 0
ans = sumnum1
 
for i in range(n):
    sumnum1 -= array[i]
    sumnum2 += array[i]
    if(ans > abs(sumnum1 - sumnum2)):
        ans = abs(sumnum1 - sumnum2)
        
 
print(ans)