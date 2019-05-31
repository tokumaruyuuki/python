num1 = int(input())
num2 = int(input())

bignum = smallnum = 0
if(num1 <= num2):
    bignum = num2
    smallnum = num1
else:
    bignum = num1
    smallnum = num2

if(bignum - smallnum <= 5):
    print(bignum - smallnum)
else:
    print((10 - bignum) + smallnum)