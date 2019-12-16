def fasctorization(n):
    arr = []
    tmp = n
    for i in range(2, int(-(-n**0.5//1)+1)):
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            arr.append([i,cnt])
    if tmp != 1:
        arr.append([tmp, 1])
    
    return arr

def nCr(n,r, mod = 10**9+7):
    r = min(n-r, r)
    nn = denom = 1
    for i in range(1,r+1):
        nn = nn * (n+1-i) % mod
        denom = denom * i % mod
    return nn * pow(denom, mod-2, mod) % mod

n,m = map(int, input().split())
fs = fasctorization(m)
mod = 10**9+7

ans = 1

for f,c in fs:
    pattern = nCr(c + n - 1, c)
    ans *= pattern
    ans %= mod
print(ans)