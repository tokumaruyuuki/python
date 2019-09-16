n,start,end = map(int,input().split(' '))
array = []
mm = int(input())
ans = 1 if mm>=start and mm<=end else 0
for i in range(n-1):
  array.append(int(input()))
for i in array:
  mm += i
  if(mm>=start and mm <= end):
      ans += 1
print(ans)
               