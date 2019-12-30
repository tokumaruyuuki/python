N = int(input())
array = list(map(int, input().split()))
evens = 0
evnes_array = []
for a in array:
    if a % 2 == 0:
        evens += 1
        cnt = 1
        while a % 2 == 0:
            a //= 2
            cnt += 1
        evnes_array.append(cnt-1)
if (evens == 0):
    print(0)
else:
    ans = sum(evnes_array)
    print(ans)
#print(evnes_array)