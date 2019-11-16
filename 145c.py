import math
n=int(input())
town=[]
ans = 0
for i in range(n):
    x,y = map(int,input().split(' '))
    town.append([x,y])
for i in range(n):
    for j in range(n):
        if(i==j):continue
        tmp= (town[i][0]-town[j][0])**2 + (town[i][1] - town[j][1])**2
        ans +=math.sqrt(tmp)*math.factorial(n-1)
print(ans/math.factorial(n))
#print(math.factorial(n))