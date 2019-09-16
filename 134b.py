a,b = map(int,input().split(' '))
ran = b*2+1
ans = a//ran if a%ran == 0 else a//ran + 1
print(ans)