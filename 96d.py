N = int(input())
ans = [1]
prime = [True] * (55556)
prime[0] = False
prime[1] = False
for i in range(55556):
    if not prime[i]:
        continue
    ans.append(i)
    p = i
    k = 2
    while (p * k) <= 55555:
        
        prime[p*k] = False
        k += 1
ans.pop(0)
ans_list = []
for p in ans:
    if p % 5 == 1:
        ans_list.append(p)
ll = list(map(str, ans_list))
print(' '.join(ll[:N]))
