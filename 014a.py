a =int(input())
b = int(input())
if(a%b == 0):
  print(0)
else:
  tmp = (a//b) + 1
  print((tmp*b) - a )