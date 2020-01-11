# coding: utf-8
# Your code here!
import itertools
n = int(input())
m,a,r,c,h = 0,0,0,0,0
for i in range(n):
    name = input()
    if name[0] == "M":
        m += 1
    elif name[0] == "A":
        a += 1
    elif name[0] == "R":
        r += 1
    elif name[0] == "C":
        c += 1
    elif name[0] == "H":
        h += 1
ll = [m,a,r,c,h]
#print(ll)
ans = 0
for i in itertools.combinations(ll, 3):
    ans += i[0] * i[1] * i[2]
print(ans)
