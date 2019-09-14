a = input()
ans = []
for i in a:
  if (i =='1'):
    ans += '9'
  else:
    ans += '1'
print(''.join(ans))