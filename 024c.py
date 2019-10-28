# coding: utf-8
# Your code here!

town, days, people = map(int, input().split(' '))
moveArray = []

for i in range(days):
    a,b = map(int,input().split(' '))
    moveArray.append([a,b])

for i in range(people):
    starttown,endtown = map(int,input().split(' '))
    flag = 1 if starttown < endtown else 0
    now = starttown
    if flag:
        cnt = 1
        for j in moveArray:
            if (j[0] <= now and now <= j[1]):
                now = j[1]
            if (now >= endtown):
                print(cnt)
                break
            cnt += 1
    else:
        cnt = 1
        for j in moveArray:
            if (j[0] <= now and now <= j[1]):
                now = j[0]
            if (now <= endtown):
                print(cnt)
                break
            cnt += 1
        