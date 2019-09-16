a,b,c = map(int, input().split(' '))
if( a==b==c):
  print(a)
elif(a==b):
  print(c)
elif(b==c):
  print(a)
else:
  print(b)