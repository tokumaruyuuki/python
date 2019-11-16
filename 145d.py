x,y = map(int,input().split(' '))
mm =max(x,y)
nn=min(x,y)
mod = 10**9+7
aa = (2*mm-nn)
if(aa%3 !=0 or aa == 0 or (x+y)%3!=0):
    print(0)
    exit()
def calc(n,mod):
    tmp = 1
    for i in range(1,n+1):
        tmp *= i
        tmp %= mod
    return tmp
pattern = aa // 3
leftpattern = mm - pattern * 2
if(leftpattern<0):
    print(0)
    exit()
#print(pattern,leftpattern)
wh = calc((pattern+leftpattern)%mod,mod)
w = calc(pattern,mod)
h = calc(leftpattern,mod)
ans = (wh*pow(w,mod-2,mod)*pow(h,mod-2,mod))%mod
print(ans)
#print(wh,w,h)