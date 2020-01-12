# coding: utf-8
# Your code here!
import numpy as np
array = [list(map(int, input().split())) for _ in range(3)]

a1 = np.asarray(array[0]) - np.asarray(array[1])
a2 = np.asarray(array[0]) - np.asarray(array[2])
a3 = np.asarray(array[1]) - np.asarray(array[2])
#print(len(set(a1)) == 1, len(set(a2)) == 1, len(set(a3)) == 1)
if not (len(set(a1)) == 1 and len(set(a2)) == 1 and len(set(a3)) == 1):
    print("No")
    exit()
array2 = np.asarray(array).T
#print(array2)
a1 = np.asarray(array2[0]) - np.asarray(array2[1])
a2 = np.asarray(array2[0]) - np.asarray(array2[2])
a3 = np.asarray(array2[1]) - np.asarray(array2[2])
if not(len(set(a1)) == 1 and len(set(a2)) == 1 and len(set(a3)) == 1):
    print("No")
    exit()
print("Yes")