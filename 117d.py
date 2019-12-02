#XXOR
n,k=map(int,input().split())
a=list(map(int,input().split()))
 
#それぞれの桁の１の数を数えていく。
flag=[0]*(40)
for u in a:
    for j in range(40):
        if (u>>j)&1==1:
            flag[j]+=1
            
#mはxの最大値。Mはそれによる得られる値。l、Lも同じ。
m=0
M=0
l=0
L=0
for i in range(40):
    if (k>>i)&1==1:
        if n>2*flag[i]:
            if M>L+(2**i)*(n-2*flag[i]):
                L=M
                l=m
            else:
                L+=(2**i)*(n-2*flag[i])
                l+=2**i
        else:
            L=m
            l=m
    if n>2*flag[i]:
        M+=(2**i)*(n-2*flag[i])
        m+=2**i
 
ans=0
for u in a:
    ans+=(u^l)
 
print(ans)