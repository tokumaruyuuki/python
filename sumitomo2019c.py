n = int(input())
times = n // 100
left = n - (times * 100)
a5 = left // 5
left -= a5 * 5
a4 = left // 4
left -= a4 * 5
a3 = left // 3
left -= a3 * 3
a2 = left // 2
left -= a2 * 2
a1 = left // 1
left -= a1 * 1
sss = a5 + a4 + a3 + a2 + a1
if(left > 0):
    sss += left
if(sss <= times):
    print(1)
else:
    print(0)