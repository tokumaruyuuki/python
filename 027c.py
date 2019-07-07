n = int(input())
cnt = 0
while n > 0:
    if cnt % 2 == 0:
        n //= 2
    else:
        n = (n - 1) // 2
    cnt += 1
print("Takahashi" if cnt % 2 == 0 else "Aoki")