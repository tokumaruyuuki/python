n = int(input())
 
array = list(map(int, input().split(" ")))
ans = 0
for i in range(1,n-1):
    mnum = max(array[i-1], array[i], array[i+1])
    minum = min(array[i-1], array[i], array[i+1])
    if(array[i] != mnum and array[i] != minum):
        ans += 1
 
 
print(ans)