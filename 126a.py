a,b = map(int, input().split())
strarray = input()

ans= []
for i in range(a):
    if (i == b-1):
        ans += strarray[i].lower()
    else:
        ans += strarray[i]
print(''.join(ans))