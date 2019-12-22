N,M = map(int, input().split())
remove_list = []
for i in range(M):
    remove_list.append(list(map(int, input().split())))
sort_list = sorted(remove_list, key = lambda x : x[1])
ans = 1
remove_bridge = [sort_list[0][1]]
for b in sort_list[1:]:
    #print(b)
    if b[0] >= remove_bridge[-1]:
        ans += 1
        remove_bridge.append(b[1])
print(ans)