n,h = map(int, input().split())
array = []
def_max = float("-inf")
for i in range(n):
    array.append(list(map(int, input().split())))
    def_max = max(array[-1][0], def_max)
array_sort0 = sorted(array, key = lambda x : x[0])
array_sort1 = sorted(array, key = lambda x : -x[1])
ans = 0 
tmp_sum = 0

for a,b in array_sort1:
    if def_max >= b or tmp_sum >= h:
        break
    else:
        ans += 1
        tmp_sum += b
diff = h - tmp_sum
if diff <= 0:
    print(ans)
    exit()
div = diff // def_max
if div * def_max == diff:
    ans += div
else:
    ans += div + 1
print(ans)