n,m = map(str,input().split())
nn = n * int(m)
mm = m * int(n)
if nn > mm:
    print(mm)
else:
    print(nn)