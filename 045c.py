import itertools

n = str(input())

sign = ["+", ""]
l = list(itertools.product(sign, repeat = len(n) - 1))

strArray = list(n)
ans = 0
for i in l:
    ll  = [None] * (len(n)*2 - 1)
    ll[::2] = strArray
    ll[1::2] = i
    ans += eval("".join(ll))
    
print(ans)