from bisect import bisect_left, bisect_right

n = int(input())

arrayA = list(map(int, input().split(" ")))
arrayB = list(map(int, input().split(" ")))
arrayC = list(map(int, input().split(" ")))
arrayA.sort()
arrayC.sort()

ans = 0
for i in arrayB:
    ans += bisect_right(arrayA, i-0.1) * (n - bisect_left(arrayC, i+0.1))
    
print(ans)