a,b,c = map(int, input().split(" "))

sumnum = a + b + c
maxnum = 0
array = [a,b,c]
if(sumnum % 2 == max(array) % 2):
    maxnum = max(array)
else:
    maxnum = max(array) + 1

tmp = (maxnum * 3) - sumnum
##print(tmp)
##print(sumnum)
##print(maxnum)
ans = int(tmp / 2) + (tmp % 2)

print(ans)