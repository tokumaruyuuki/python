N = int(input())
array = list(map(int, input().split()))
ans = 0
right = 0
sumnum = 0
for i in range(N):
    while right < N and (sumnum ^ array[right]) == (sumnum + array[right]):
        sumnum += array[right]
        right += 1
    ans += right - i
    if right == i:
        right += 1
    else:
        sumnum -= array[i]
print(ans)