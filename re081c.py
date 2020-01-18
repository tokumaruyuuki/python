n,k = map(int, input().split())
array = list(map(int, input().split()))
ans = 0
dic = {}
for a in array:
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1

sort_dict = sorted(dic.items(), key = lambda x : x[1])
#print(sort_dict)
for i in range(len(dic) - k):
    ans += sort_dict[i][1]
print(ans)
