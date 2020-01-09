# coding: utf-8
# Your code here!

N = int(input())
array = list(map(int, input().split()))
array.insert(0,0)
array.append(0)
ans_sum = 0
for i in range(N+2):
    ans_sum += abs(array[i-1] - array[i])

for i in range(1, N+1):
    ans = ans_sum - (abs(array[i] - array[i-1]) + abs(array[i+1] - array[i])) + abs(array[i-1] - array[i+1])
    print(ans)
