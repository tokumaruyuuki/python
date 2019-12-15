# coding: utf-8
# Your code here!
def gcd(a,b):
    while b != 0:
        a,b = b,a%b
    
    return a
city, position = map(int, input().split())
array = list(map(int, input().split()))
array.append(position)
array.sort()
ans = array[1] - array[0] if len(array) >= 2 else array[0]
#print(array)
for i in range(2,city+1):
    #print(i)
    #print(array[i],array[i-1], ans)
    a = max(ans, array[i] - array[i-1])
    b = min(ans, array[i] - array[i-1])
    ans = gcd(a,b)
print(ans)