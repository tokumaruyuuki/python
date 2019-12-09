import numpy as np
n = int(input())
num_list = np.array(input().split(), dtype = np.int64)
mod = 10**9+7
ans = 0
for i in range(60):
    one_cnt = np.count_nonzero(num_list >> i & 1)
    ans += 2 ** i * (one_cnt * (n - one_cnt))
    ans %= mod
print(ans)