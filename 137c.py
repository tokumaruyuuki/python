n = int(input())
array = {}
ans = 0
for i in range(n):
    tmp = list(input())
    tmp.sort()
    tmp = ''.join(tmp)
    if (tmp in array):
        ans += array[tmp]
        array[tmp] += 1
    else:
        array[tmp] = 1
print(ans)