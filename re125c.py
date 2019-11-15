def gcd(a,b):
    while b:
        a,b = b, a%b
    return a

n=int(input())
array=list(map(int,input().split(' ')))
left = [0] * (n+1)
right = [0] * (n+1)
for i in range(n):
    left[i+1] = gcd(left[i],array[i])
for i in reversed(range(n)):
    right[i] = gcd(right[i+1],array[i])
ans = []
for i in range(n):
    ans.append(gcd(left[i], right[i+1]))
print(max(ans))