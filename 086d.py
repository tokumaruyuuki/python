"""
参考記事：https://qiita.com/convexineq/items/afc84dfb9ee4ec4a67d5
"""

import numpy as np
n,k = map(int, input().split())
grid = [[0] * (2*k+1) for _ in range(2*k+1)]
mod = 2 * k
def make_pattern(x):
    if x < k-1:
        return [[0, x+1], [x+k+1, 2*k]]
    else:
        return [[x-k+1, x+1]]


for i in range(n):
    x, y, c = input().split()
    x = int(x)
    y = int(y)
    if c == "W":
        #x += k
        y += k
    x %= mod
    y %= mod
    for m  in [0,k]:
        #print(make_pattern((m+x)%mod))
        for l,r in make_pattern((m+x)%mod):
            for d,u in make_pattern((m+y)%mod):
                grid[l][d] += 1
                grid[l][u] -= 1
                grid[r][d] -= 1
                grid[r][u] += 1
#print(grid)
ans = np.max(np.cumsum(np.cumsum(grid, axis=0), axis = 1))
print(ans)