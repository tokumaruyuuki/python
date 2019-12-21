n = int(input())
ans = []
if n == 0:
    print(0)
else:
    while n:
        if n % 2 != 0:
            n -= 1
            ans.append('1')
        else:
            ans.append('0')
        n /= -2
    ans.reverse()
    print(''.join(ans))