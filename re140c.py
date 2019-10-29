n = int(input())
array = list(map(int,input().split(' ')))
ansList = [array[0]]
for i in range(1,n-1):
    ansList.append(min(array[i],array[i-1]))
ansList.append(array[-1])
print(sum(ansList))