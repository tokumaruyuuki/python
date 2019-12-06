pre, city = map(int, input().split())
ans_list = []

for i in range(city):
    a, b = map(int, input().split())
    ans_list.append([i,a-1,b])

prefectures = [1] * (pre)
ans_list = sorted(ans_list, key = lambda x:x[2])
for i in range(city):
    ans_list[i] = [ans_list[i][0], ans_list[i][1],prefectures[ans_list[i][1]]]
    prefectures[ans_list[i][1]] += 1
ans_list = sorted(ans_list, key = lambda x:x[0])

for ind,prefecture_num, cities in ans_list:
    prefecture_num += 1
    tmp1 = str(prefecture_num).zfill(6)
    tmp2 = str(cities).zfill(6)
    print(tmp1 + tmp2)