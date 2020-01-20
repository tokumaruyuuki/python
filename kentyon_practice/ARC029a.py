import itertools
n = int(input())
meats = [int(input()) for _ in range(n)]
ans = float('inf')
for v in itertools.permutations(meats):
    times = 0
    if n == 1:
        times = v[0]
    elif n == 2:
        times = max(v[0], v[1])
    elif n == 3:
        times = max(v[0] + v[1], v[2])
    else:
        times = min(max(v[0] + v[1], v[2] + v[3]), max(v[0] + v[1] + v[2], v[3]))
    ans = min(ans, times)
    
print(ans)