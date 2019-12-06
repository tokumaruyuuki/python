from itertools import product
high, para, target = map(int, input().split())
mod = 10**9 + 7
def binary(m):
    ret = 0
    if(m <= 0):
        return 1
    for pattern in product([0,1], repeat = m):
        p = ''.join(list(map(str, pattern)))
        if '11' not in p:
            ret += 1
    return ret

amida = [[0] * para for i in range(high+1)]
amida[0][0] = 1
for h in range(high):
    for w in range(para):
        amida[h+1][w] = (amida[h+1][w] + amida[h][w] * binary(w-1) * binary(para - w - 2)) % mod
        if w+1 <= para-1:
            amida[h+1][w+1] = (amida[h+1][w+1] + amida[h][w] * binary(w-1) * binary(para - w - 3)) % mod
        elif w-1 >= 0:
            amida[h+1][w-1] = (amida[h+1][w-1] + amida[h][w] * binary(w-2) * binary(para - w - 2)) % mod

print(amida[high][target-1])
-----------------------------------------------


from itertools import product
high, para, target = map(int, input().split())
mod = 10**9 + 7
def binary(w):
    if w <= 0:
        return 1
    ret = 0
    for pattern in product([0, 1], repeat=w):
        pattern = ''.join(list(map(str, pattern)))
        if '11' not in pattern:
            ret += 1
    return ret
 
amida = [[0] * para for i in range(high+1)]
amida[0][0] = 1
for h in range(high):
    for w in range(para):
        amida[h + 1][w] = (amida[h + 1][w] + amida[h][w] * binary(w - 1) * binary(para - w - 2)) % mod
        if w+1 <para:
            amida[h+1][w+1] = (amida[h+1][w+1] + amida[h][w] * binary(w-1) * binary(para - w - 3)) % mod
        if w-1 >= 0:
            amida[h+1][w-1] = (amida[h+1][w-1] + amida[h][w] * binary(w-2) * binary(para - w - 2)) % mod
 
print(amida[high][target-1] % mod)