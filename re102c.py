n = int(input())
tmparray = list(map(int, input().split()))
array = [0] * n
for i in range(n):
    array[i] = tmparray[i] - (i+1)
array.sort()
b = array[n//2]
ans = 0
for a in array:
    ans += abs(a - b)
print(ans)