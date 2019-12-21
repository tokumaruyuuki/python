boxs, childrens = map(int, input().split())
candies = list(map(int,input().split()))

sum_array = [0] * boxs
for i in range(boxs):
    sum_array[i] = (candies[i] + sum_array[i-1]) % childrens
#print(sum_array)
mod_array = {}
ans = 0
for i in range(boxs):
    if sum_array[i] in mod_array:
        mod_array[sum_array[i]] += 1
        ans += (mod_array[sum_array[i]] - 1) if sum_array[i] != 0 else mod_array[0]
    elif sum_array[i] % childrens == 0:
        mod_array[sum_array[i]] = 1
        ans += mod_array[sum_array[i]]
    else:
        mod_array[sum_array[i]] = 1
#print(mod_array)
print(ans)