n = int(input())
array = list(map(int,input().split()))
sumnum = sum(array)
left=array
sumL = sum(left)
sumR = 0
ans_array = [abs(sumL-sumR)]
for i in reversed(range(n)):
    sumL-=array[i]
    sumR+=array[i]
    ans_array.append(abs(sumL-sumR))
ans_array.sort()
print(ans_array[0])