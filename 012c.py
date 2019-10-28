# coding: utf-8
# Your code here!

n = int(input())
baseNumber = 2025
diffNum = baseNumber - n
for i in range(1,10):
    for j in range(1,10):
        if ( i*j == diffNum):
            print(str(i) + ' x ' + str(j))