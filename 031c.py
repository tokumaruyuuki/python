n = int(input())
array = list(map(int, input().split(" ")))

takahasi = -float('inf')
for i in range(n):
    tmpTkahasi = -float('inf')
    tmpAoki = -float('inf')
    for j in range(n):
        tmp1 = 0
        tmp2 = 0
        if(i == j):
            continue
        start = min(i,j)
        end = max(i,j)
        odd = start % 2 
        for g in range(start, end+1):
            if(g % 2 == odd):
                tmp1 += array[g]
            else:
                tmp2 += array[g]
        if(tmp2 > tmpAoki):
            tmpTkahasi = tmp1
            tmpAoki = tmp2
    takahasi = max(takahasi,tmpTkahasi)

print(takahasi)