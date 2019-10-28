# coding: utf-8
# Your code here!
n = int(input())
slimes = input()
ans = len(slimes)
for i in range(1,n):
    if(slimes[i] == slimes[i-1]):
        ans -= 1
print(ans)