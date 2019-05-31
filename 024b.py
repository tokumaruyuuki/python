tmp = input().split(" ")
member = int(tmp[0])
seconds = int(tmp[1])
array = [0] * 1100001

for i in range(member):
    tmp2 = int(input())
    array[tmp2] += 1
    array[tmp2+seconds] -= 1

ans = 0
nowStatus = 0
for i in range(1100001):
    nowStatus += array[i]
    if(nowStatus >= 1):
        ans += 1

print(ans)