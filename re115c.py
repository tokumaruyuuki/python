# coding: utf-8
# Your code here!

trees, cnt = map(int, input().split())
array = []
for _ in range(trees):
    array.append(int(input()))
array.sort()
ans = float('inf')
for i in range(trees-cnt+1):
    tmp = array[i+cnt-1] - array[i]
    ans = min(tmp,ans)
print(ans)