dog, monkey = map(int, input().split(" "))

if (dog == monkey):
    ans = 1
    for i in range(1,dog+1):
        ans *= i * i
        tmp = int(ans % (10**9 + 7))
        ans = tmp
    ans *= 2
    print(int(ans % (10**9 + 7)))
elif (abs(dog - monkey) == 1):
    ans = 1
    a = dog if(dog <= monkey) else monkey
    for i in range(1,a+1):
        ans *= i * i
        tmp = int(ans % (10**9 + 7))
        ans = tmp
    ans *= (a + 1)
    print(int(ans % (10**9 + 7)))
else:
    print(0)