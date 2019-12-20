# coding: utf-8
# Your code here!
n = input()
k = input()
if k == '1':
    print(n[0])
else:
    for i in range(min(len(n), int(k))):
        if n[i] != '1':
            print(n[i])
            exit()
    else:
        print(1)