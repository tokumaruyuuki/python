a,b = map(int,input().split(' '))
ans = 2019
if(b - a >= 2019):
    print(0)
else:
    for i in range(a,b+1):
        for j in range(i+1,b+1):
            ans = min(ans,(i*j)%2019)
            if(ans ==0):break
    print(ans)