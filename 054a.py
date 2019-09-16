a,b = map(int,input().split(' '))
if(a == b ):
  print('Draw')
elif(a == 1):
  print('Alice')
elif(b == 1):
  print('Bob')
else:
  ans = 'Alice' if (a > b) else 'Bob'
  print(ans)
  