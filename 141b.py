odd = ['R','U','D']
even = ['L','U','D']
s = input()
for i in range(1,len(s)+1):
    if(i%2 == 0):
        if(s[i-1] not in even):
            print('No')
            break
    else:
        if(s[i-1] not in odd):
            print('No')
            break
else:
    print('Yes')