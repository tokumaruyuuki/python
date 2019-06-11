n = int(input())

flag = 0 
nowSecomd, nowx, nowy = map(int, input().split(" "))
if(n == 1):
    if(nowSecomd < nowx + nowy or nowSecomd % 2 != (nowx + nowy) % 2):
        print("No")
    else:
        print("Yes")
else:
    for i in range(n-1):
        second, x, y  = map(int, input().split(" "))
        sumlength = abs(nowx - x) + abs(nowy - y)
        diffSecond = second - nowSecomd
        if(sumlength == 0 and diffSecond % 2 == 1):
            flag = 1
            break
        if(diffSecond < sumlength or diffSecond % 2 != sumlength % 2):
            flag = 1
            break
        nowSecomd = second
        nowx = x
        nowy = y
    
    if(flag == 0):
        print("Yes")
    else:
        print("No")