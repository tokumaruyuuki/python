# coding: utf-8
# Your code here!

# coding: utf-8
# Your code here!
import fractions
a,b,c,d = map(int,input().split(' '))
divmax = max(c,d)
divmin = min(c,d)

minus1 = b//divmax - (a-1)//divmax
minus2 = b//divmin - (a-1)//divmin

multiple = (c*d) // fractions.gcd(c,d)
ans = (b-a+1) - minus1 - minus2 + (b//multiple - (a-1)//multiple)
print(ans)

#print(multiple)
#print(minus1)

#print(minus2)