n = int(input())
dic = {}
for i in range(n):
    ttmp = list(input())
    ttmp.sort()
    tmp = ''.join(ttmp)
    if(tmp in dic):
        dic[tmp] += 1
    else:
        dic[tmp] = 1
ans = 0
#print(dic)
for k,v in dic.items():
    if(v <=1):continue
    ans += (v-1)*v // 2
print(ans)