n,h = map(int,input().split(' '))
a,b,c,d,e = map(int,input().split(' '))
ans = float('inf')
for i in range(n):
    tmpAns = a * i
    plus = max(0,((((e*n - (h + (b+e)*i)) // (d+e))) + 1))
    ans = min(ans,tmpAns + plus * c)
print(ans)