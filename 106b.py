N = int(input())
 
ans = 0
for i in range(1,N+1):
    if i % 2 ==1:
        cnt = 0
        for j in range(i):
            if i%(j+1) == 0:
                cnt += 1
        if cnt == 8:
            ans += 1
 
print(ans)