n = int(input())
left = 1000-n
ans = 0
while left != 0:
    for i in [500,100,50,10,5,1]:
        if left >=i:
            left -= i
            ans += 1
            break
print(ans)