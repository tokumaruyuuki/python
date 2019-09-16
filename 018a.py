array = []
for i in range(3):
  array.append(int(input()))
array2 = sorted(array,reverse = True)          

for i in range(3):
  print(array2.index(array[i]) +1)