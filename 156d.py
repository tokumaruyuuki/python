n,a,b=map(int,input().split())
m=10**9+7
def cmb(x,y):
    c=1
    for i in range(1,y+1):
      c=(c*(x-i+1)*pow(i,m-2,m))%m
    return c
print((pow(2,n,m)-1-cmb(n,a)-cmb(n,b))%m)