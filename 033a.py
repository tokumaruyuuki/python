n = input()
ans =0 
for i in n:
  if n[0] != i:
    ans += 1
if(ans >=1):
  print('DIFFERENT')
else:
  print('SAME')