a,b,c = map(int, input().split(" "))
 
x = a + b
y = b + c
z = c + a
print(min(x,y,z))