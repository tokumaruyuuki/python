n = int(input())
array = list(map(int, input().split()))
dic = {}
for a in array:
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1
ans = 0
for k,v in dic.items():
    if k > v:
        ans += v
    elif k < v:
        ans += (v - k)
        
        
print(ans)