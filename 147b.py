s = input()
leng = len(s)
ans =0
if(leng % 2 == 0):
    a1 = s[:leng//2]
    a2 = list(s[leng//2:])
    a2.reverse()
    a2 = ''.join(a2)
    #print(a1,a2)
    for i in range(leng//2):
        if(a1[i] != a2[i]):
            ans += 1
else:
    a1 = s[:leng//2]
    a2 = list(s[leng//2+1:])
    a2.reverse()
    a2 = ''.join(a2)
    #print(a1,a2)
    for i in range(leng//2):
        if(a1[i] != a2[i]):
            ans += 1
    
print(ans)