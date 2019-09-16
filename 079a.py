n = input()
first = n[0]
second = n[1]
if((first == n[1] and first == n[2]) or (second == n[2] and second == n[3])):
  print('Yes')
else:
  print('No')