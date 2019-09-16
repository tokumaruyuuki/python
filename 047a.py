a = list(map(int, input().split(' ')))
if(a[0] + a[1] == a[2] or a[1] + a[2] == a[0] or a[2] + a[0] == a[1]):
  print('Yes')
else:
  print('No')