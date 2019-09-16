a,b = map(int,input().split(' '))
start = b - a + 1
end = b + a - 1
for i in range(start, end):
  print(' %d'%i, end='')
print(' %d'%end)