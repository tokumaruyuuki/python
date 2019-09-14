n = int(input())
array1 = list(map(int, input().split(' ')))
array2 = list(map(int,input().split(' ')))
array3 = list(map(int, input().split(' ')))
ans = 0

for i in range(n):
    if(i != 0 and array1[i] == array1[i-1] + 1):
      ans += array3[array1[i-1]-1]
    ans += array2[array1[i]-1]
print(ans)