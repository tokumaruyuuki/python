a,b,c = map(int,input().split(' '))
aa = [abs(a-b), abs(a-c), abs(b-c)]
ma = max(aa)
print(sum(aa) - ma)