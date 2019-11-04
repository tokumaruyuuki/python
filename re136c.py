mass = int(input())
array = list(map(int,input().split(' ')))

falg=True
for i in reversed(range(1,mass)):
    if(array[i-1] > array[i]):
        array[i-1] -= 1
    if(array[i-1] > array[i]):
        falg = False
        #print(array[i-1],i)
        break
ans = "Yes" if(falg) else "No"
print(ans)
#print(array)