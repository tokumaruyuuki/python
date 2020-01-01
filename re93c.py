a,b,c = map(int, input().split())
ALL = a + b + c
maxx = max(a,b,c)
ALL2 = maxx*3
if ALL % 2 == ALL2 % 2:
    array = [a,b,c]
    array.sort()
    top = array[2]
    center = array[1]
    bottom = array[0]
    add = top - center
    bottom += add
    ans = add
    diff = top - bottom
    while diff > 1:
        diff -= 2
        ans += 1
    ans += diff
    print(ans)
else:
    array = [a,b,c]
    array.sort()
    top = array[2]
    center = array[1]
    bottom = array[0]
    add = top + 1 - center
    bottom += add
    ans = add + 1
    diff = top - bottom
    while diff > 1:
        diff -= 2
        ans += 1
    ans += diff
    print(ans)