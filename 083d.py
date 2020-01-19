# coding: utf-8
# Your code here!
s=input()
lens = len(s)
if lens % 2 == 0:
    if s[lens//2-1] != s[lens//2]:
        print(lens//2)
        exit()
    target = s[lens//2-1]
    for i in range(2,lens//2):
        if s[lens//2+i-1] != target or s[lens//2-i] != target:
            print(lens//2+i-1)
            exit()
    else:
        print(lens)
else:
    target = s[lens//2]
    for i in range(1,lens//2+1):
        if s[lens//2 - i] != target or s[lens//2 + i] != target:
            print(lens//2+i)
            exit()
    else:
        print(lens)