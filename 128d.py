import copy
length, times = map(int,input().split(' '))
array = list(map(int, input().split(' ')))
reversedarray = list(reversed(array))
ans = 0
trytimes = min(length,times)
for a in range(trytimes+1):
    for b in range(trytimes-a+1):
        copyArray = copy.copy(array)
        throw = times - (a+b)
        #tmpsum = array[0:a] + reversedarray[0:b]
        #print(copyArray)
        tmpsum = []
        for i in range(a):
            tmpsum.append(copyArray.pop(0))
            #print(copyArray)
        for j in range(b):
            tmpsum.append(copyArray.pop(-1))
        #print(a,b,tmpsum)
        tmpsum.sort()
        #print(tmpsum)
        #print(b,reversedarray[0:b])
        sumarray = []
        for n in tmpsum:
            if(n<0 and throw>0):
                throw-=1
                continue
            sumarray.append(n)
        #print(throw,tmpsum)
        #print(tmpsum)
        #print(sumarray)
        ans = max(sum(sumarray), ans)
print(ans)
        