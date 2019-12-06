# coding: utf-8
# Your code here!

n = int(input())
div = [0] * (n+1)
ans = 0
def make_divisors(n):
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            div[i] += 1
            if i != n // i:
                div[n//i] += 1

for i in range(1, n+1):
    make_divisors(i)
print(div)
cnt75 = div.count(74)
cnt25 = div.count(24)
cnt15 = div.count(14)
cnt5 = div.count(4)
cnt3 = div.count(2)
print(cnt75, cnt25, cnt15, cnt5, cnt3)
ans += (cnt5-1) * (cnt5) * cnt3 if cnt5 >= 1 else 0
ans += cnt5 * cnt15
ans += cnt25 * cnt3
ans += cnt75

print(ans)
--------------------------
n = int(input())

prime = [0] * (n+1)

for i in range(2, n+1):
    origin_num = i
    for j in range(2, i+1):
        while origin_num % j == 0 :
            prime[j] += 1
            origin_num //= j

def search(a):
    return len(list(filter(lambda x: x >= a-1, prime)))
#print(prime)
ans = (search(75) + (search(25) * (search(3) - 1)) + (search(15) * (search(5) - 1)) + (search(5) * (search(5) - 1) * (search(3) - 2)) // 2)
print(ans)