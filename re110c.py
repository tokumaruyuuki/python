# coding: utf-8
# Your code here!

#import string
#alp_list = [chr(i) for i in range(97, 97+26)]
alp_s = {}
alp_t = {}
s = input()
t = input()
for i in range(len(s)):
    if s[i] not in alp_t:
        alp_t[s[i]] = t[i]
    else:
        if alp_t[s[i]] != t[i]:
            print('No')
            break
    if t[i] not in alp_s:
        alp_s[t[i]] = s[i]
    else:
        if alp_s[t[i]] != s[i]:
            print('No')
            break
else:
    print('Yes')