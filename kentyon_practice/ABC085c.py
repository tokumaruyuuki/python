n,y = map(int,input().split())
for i in range(n+1):
    for j in range(n+1):
        left = n - i - j
        if left <0:
            continue
        sum_money = (i*10000 + j * 5000 + left * 1000)
        if sum_money == y:
            print(i,j,left)
            exit()
else:
    print(-1,-1,-1)