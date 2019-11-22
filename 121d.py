# coding: utf-8
# Your code here!
a,b = map(int,input().split())
if(a==b):
    print(a)
    exit()
start = 0
end1 = a-1
end2 = b
def calc_xor(start,end):
    evens = (end+1) // 2
    if(end%2==0):
        if(evens%2==0):
            return end
        else:
            return end + 1
    else:
        if(evens%2==0):
            return end - 1
        else:
            return end

def binary_num(num1,num2):
    return bin(num1^num2)

x1 = calc_xor(start, end1)
x2 = calc_xor(start, end2)
ans = binary_num(x1, x2)
#print(x1,x2)
print(int(ans, 0))

WA 
----------------------------------------
a, b = list(map(int, input().split()))
ans = 0
if a % 2 == 1:
    ans, a = a, a + 1
c = b - a + 1
if (c // 2) % 2 == 0:
    ans ^= 0
else:
    ans ^= 1
if c % 2 == 1:
    ans ^= b
print(ans)