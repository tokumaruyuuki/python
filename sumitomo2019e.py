n = int(input())
array = list(map(int, input().split()))
a1 = 0
a2 = 0
a3 = 0
ans = 1
pre = 1
for i in array:
    cnt = 0
    candi = []
    if(i==a1):
        cnt += 1
        candi.append(1)
    if(i==a2):
        cnt += 1
        candi.append(2)
    if(i==a3):
        cnt += 1
        candi.append(3)
    first = candi[0] if(not len(candi) == 0) else 1
    if(first == 1):
        a1 += 1
    elif(first == 2):
        a2 += 1
    else:
        a3 += 1
    ans *= cnt
    ans %= 1000000007
#print(i,ans,cnt)
 
#print(a1,a2,a3)
#ans_list = [a1,a2,a3]
#ll = list(set(ans_list))
print(ans)