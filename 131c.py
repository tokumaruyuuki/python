import fractions
 
minnum,maxnum,div1,div2 = map(int, input().split(" "))
 
num1 = (minnum - 1) // div1
num2 = maxnum // div1
num3 = (minnum - 1) // div2
num4 = maxnum // div2
lcm =  div1 * div2 // fractions.gcd(div1, div2)
num5 = (minnum  - 1)// lcm
num6 = (maxnum // lcm)
 
#print(num1)
#print(num2)
#print(num3)
#print(num4)
#print(num5)
#print(num6)
ans = (num4 - num3) + (num2 - num1)
 
print((maxnum - minnum) + 1 - ans + (num6 - num5))