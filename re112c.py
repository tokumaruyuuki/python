n = int(input())
array = []
cnt = 0
for _ in range(n):
    x,y,h = map(int,input().split())
    array.append([x,y,h])
    if h >= 1:
        cnt += 1

if cnt == 1:
    flag = True
else:
    flag = False
if flag:
    for xx, yy, hh in array:
        if hh > 0:
            print(xx,yy,hh)
            exit()

for x in range(101):
    for y in range(101):
        tmp_ans_cnadidate = []
        for xx,yy,hh in array:
            if(hh <= 0):
                continue
            cnt += 1
            tmp_ans = abs(xx-x) + abs(yy-y) + hh
            if(len(tmp_ans_cnadidate) == 0):
                tmp_ans_cnadidate.append(tmp_ans)
            elif(tmp_ans_cnadidate[0] != tmp_ans):
                break
        else:
            print(x,y,tmp_ans_cnadidate[0])