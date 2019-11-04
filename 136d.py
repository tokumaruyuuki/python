# coding: utf-8
# Your code here!

array = list(input())
l = len(array)
ans = [0] * l
rarray = []
larray = []
for i in range(l):
    if(array[i] == 'L'):
        for j in rarray:
            if((i - j) % 2 == 0):
                ans[i] += 1
            else:
                ans[i-1] += 1
        rarray = []
    else:
        rarray.append(i)
#print(ans)
for i in reversed(range(l)):
    #print(larray)
    if(array[i] == 'R'):
        for j in larray:
            #print(larray)
            if((j - i) % 2 == 0):
                ans[i] += 1
            else:
                ans[i+1] += 1
        larray = []
    else:
        larray.append(i)
ansArray = list(map(str,ans))

print(' '.join(ansArray))