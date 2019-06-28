tate, yoko = map(int, input().split(" "))

maxnum = float('inf')
for i in range(1,tate):
    tmp = i * yoko
    sub1 = (tate-i)//2
    sub2 = tate - (sub1 + i)
    tmpmax1 = max(tmp, sub1 * yoko, sub2 * yoko)
    tmpmin1 = min(tmp, sub1 * yoko, sub2 * yoko)
    maxnum = min(maxnum, tmpmax1- tmpmin1)
    sub3 = yoko//2
    sub4 = yoko - sub3
    tmpmax2 = max(tmp, sub3 * (tate-i), sub4 * (tate-i))
    tmpmin2 = min(tmp, sub3 * (tate-i), sub4 * (tate-i))
    maxnum = min(maxnum, tmpmax2 - tmpmin2)

tate,yoko = yoko, tate
for i in range(1,tate):
    tmp = i * yoko
    sub1 = (tate-i)//2
    sub2 = tate - (sub1 + i)
    tmpmax1 = max(tmp, sub1 * yoko, sub2 * yoko)
    tmpmin1 = min(tmp, sub1 * yoko, sub2 * yoko)
    maxnum = min(maxnum, tmpmax1- tmpmin1)
    sub3 = yoko//2
    sub4 = yoko - sub3
    tmpmax2 = max(tmp, sub3 * (tate-i), sub4 * (tate-i))
    tmpmin2 = min(tmp, sub3 * (tate-i), sub4 * (tate-i))
    maxnum = min(maxnum, tmpmax2 - tmpmin2)

print(maxnum)