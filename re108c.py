n, k = map(int, input().split())
if k % 2 == 0:
    num_list = []
    half_num_list = []
    for i in range(1,n+1):
        if i % k == k // 2:
            half_num_list.append(i)
        elif i % k == 0:
            num_list.append(i)
    #print(num_list)
    #print(half_num_list)
    ans = len(num_list) ** 3
    ans += len(half_num_list) ** 3
else:
    num_list = []
    for i in range(1,n+1):
        if i % k == 0:
            num_list.append(i)
    ans = len(num_list) ** 3
print(ans)