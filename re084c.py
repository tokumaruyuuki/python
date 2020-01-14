# coding: utf-8
# Your code here!
n = int(input())
# [開始時間、タイミング、距離]
trains = [] * (n-1)
first_seconds = 0
for i in range(n-1):
    a,b,c = map(int, input().split())
    trains.append([b,c,a])

for i in range(n-1):
    ans_seconds = 0
    for j in range(i,n-1):
        a,b,c = trains[j][2],trains[j][0], trains[j][1]
        if ans_seconds == 0:
            ans_seconds += b + a
        else:
            if ans_seconds >= b:
                if ans_seconds % c == 0:
                    ans_seconds += a
                else:
                    ans_seconds = ((ans_seconds // c) + 1) * c  + a
            else:
                ans_seconds = b + a
    print(ans_seconds)
print(0)