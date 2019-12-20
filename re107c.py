# coding: utf-8
# Your code here!

n, k = map(int, input().split())
array = list(map(int, input().split()))
ans = float('inf')
for i in range(n - k + 1):
    ans = min(ans, array[i + k - 1] - array[i] + abs(array[i]), array[i + k -1] - array[i] + abs(array[i + k - 1]))
print(ans)