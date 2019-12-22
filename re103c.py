n = int(input())
array = list(map(int, input().split()))
num =1
for a in array:
    num *= a
num -=1 
ans = 0
for a in array:
    ans+= num % a
print(ans)