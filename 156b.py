n,k = map(int, input().split())
cnt = 0
t = 0
while n != 0:
    n //= k
    t += 1
    cnt += 1
    
print(cnt)