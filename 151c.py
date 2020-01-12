n,m = map(int,input().split())
ac = 0
wa = 0
ll = [True] * n
al = [False] * n
wl = [0] * n
for i in range(m):
    a,b = input().split()
    if ll[int(a)-1]:
        if b == "AC":
            ac+=1
            ll[int(a)-1] = False
            al[int(a)-1] = True
        else:
            wl[int(a)-1] += 1
for i in range(n):
    if al[i]:
        wa += wl[i]
print(ac,wa)