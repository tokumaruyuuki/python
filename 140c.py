n = int(input())
inarray = list(map(int,input().split(' ')))
array = [inarray[0]]
for i in range(1,n-1):
    array.append(min(inarray[i-1],inarray[i]))
array.append(inarray[-1])
print(sum(array))