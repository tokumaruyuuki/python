n = int(input())
array = list(map(int,input().split()))
ans, diff, h_last = 0,0,0

for i in array:
    if i < h_last:
        ans += h_last - diff
        diff = i
    h_last = i
print(ans + array[-1] - diff)