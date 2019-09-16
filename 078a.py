array = ['A', 'B', 'C', 'D', 'E', 'F']
a = input().split(' ')
aa = array.index(a[0])
bb = array.index(a[1])
if(aa == bb):
  print('=')
elif(aa < bb ):
  print('<')
else:
  print('>')