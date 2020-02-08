import string
ll = string.ascii_lowercase
st = list(input())
if st == ['a']:
    print(-1)
elif len(st) == 1:
    print(ll[ll.index(st[0])-1])
else:
    print(''.join(st[:len(st)-1]))