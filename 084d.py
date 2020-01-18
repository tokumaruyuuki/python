q = int(input())
array = [0] * (10**5+1)
prime = [True] * (10**5+1)
prime[0] = False
prime[1] = False
for i in range(10**5+1):
    if prime[i]:
        k = i
        tmp = i
        k *= tmp
        while k <= 10**5:
            prime[k] = False
            k += tmp

for i in range(1, 10**5+1, 2):
    array[i] = array[i-2]
    if prime[i] and prime[(i+1) // 2]:
        array[i] += 1
    #print(i,prime[i], prime[(i+1)//2], array[i])
    #if i == 100:
    #    break
for i in range(q):
    l,r = map(int, input().split())
    #print(array[r], array[l-2])
    print(array[r] - array[l-2])