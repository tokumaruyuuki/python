n = int(input())
time,x,y = 0,0,0
for i in range(n):
    t, xx, yy = map(int, input().split())
    diffx = abs(x-xx)
    diffy = abs(y-yy)
    if t - time < diffx + diffy:
        print("No")
        exit()
    if (t - time) % 2 != (diffx + diffy) % 2:
        print("No")
        exit()
    time,x,y = t,xx,yy
else:
    print("Yes")