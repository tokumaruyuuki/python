k,s = map(int, input().split())
ans = 0
for i in range(k+1):
    for j in range(k+1):
        left = s - (i+j)
        if left < 0 or left > k:
            continue
        ans += 1
        #print(i,j,left)
print(ans)