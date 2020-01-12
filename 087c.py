import numpy as np
n = int(input())
array = list(map(int, input().split()))
array2 = list(map(int, input().split()))
sum_a2 = np.cumsum(array2)

ans = 0
tmp_sum = 0
for i in range(n):
    tmp_sum += array[i]
    ans = max(ans, tmp_sum + sum_a2[-1] - sum_a2[i-1]) if i > 0 else max(ans, tmp_sum + sum_a2[-1])
print(ans)