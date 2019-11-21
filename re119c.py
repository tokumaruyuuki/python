# coding: utf-8
# Your code here!
import itertools
n,a,b,c = map(int,input().split(' '))
bambboo = []
for _ in range(n):
    bambboo.append(int(input()))
combination = list(itertools.product(range(4), repeat=n))
#0=なし　1=A 2=B 3=C 
ans = float('inf')
for cc in combination:
    if(not {1,2,3} <= set(cc)):
        continue
    aArray = []
    bArray = []
    cArray = []
    for index,i in enumerate(cc):
        if(i==1):
            aArray.append(bambboo[index])
        elif(i==2):
            bArray.append(bambboo[index])
        elif(i==3):
            cArray.append(bambboo[index])
    a_sum = abs(sum(aArray) - a) + (len(aArray) - 1)*10
    b_sum = abs(sum(bArray) - b) + (len(bArray) - 1)*10
    c_sum = abs(sum(cArray) - c) + (len(cArray) - 1)*10
    ans = min(ans,a_sum+b_sum+c_sum)
print(ans)