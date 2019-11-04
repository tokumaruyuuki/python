import heapq
jobs, days = map(int,input().split(' '))
array = [[] for _ in range(days)]

for i in range(jobs):
    day,money = map(int,input().split(' ')) 
    if(day > days):continue
    array[day-1].append(money * -1)

ans = 0 
que = []
for i in range(days):
    for m in array[i]:
        heapq.heappush(que,m)
    if(que):
        ans -= heapq.heappop(que)
print(ans)