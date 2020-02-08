n = int(input())
ll = []
for i in range(n):
    a = int(input())
    if not ll:
        ll.append(a)
        continue
    else:
        for j in range(len(ll)):
            if ll[j] >= a:
                ll[j] = a
                break
        else:
            ll.append(a)
            ll.sort()
print(len(ll))