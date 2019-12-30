N,M = map(int, input().split())
x,y,z = [],[],[]
for i in range(N):
    _x,_y,_z = map(int, input().split())
    x.append(_x)
    y.append(_y)
    z.append(_z)
cndidate = []
for xx in [1,-1]:
    for yy in [1,-1]:
        for zz in [1,-1]:
            score = list(map(sum, zip([xx * x for x in x],
                                            [yy * y for y in y],
                                            [zz * z for z in z])))
            score.sort(reverse=True)
            cndidate.append(sum(score[:M]))
print(max(cndidate))
       