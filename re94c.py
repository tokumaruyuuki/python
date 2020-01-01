N = int(input())
array = list(map(int, input().split()))
sort_array = sorted(array)
half = sort_array[N//2 - 1]

for i in range(N):
    if array[i] <= half:
        print(sort_array[N//2])
    else:
        print(half)