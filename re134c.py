n = int(input())
array = []

for i in range(n):
    tmp = int(input())
    array.append(tmp)
tmp = sorted(array)
maxnum = tmp[-1]
maxnum2 = tmp[-2]
cnt = array.count(maxnum)
if(cnt >= 2):
    for _ in range(n):
        print(maxnum)
else:
    for i in range(n):
        if(array[i] == maxnum):
            print(maxnum2)
        else:
            print(maxnum)
            
