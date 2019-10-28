# coding: utf-8
# Your code here!
a,b = map(int,input().split(' '))

def makeDiv(n):
    div = []
    for i in range(1,int(n**0.5)+1):
        if(n % i == 0):
            div.append(i)
            if(i != n //i):
                div.append(n//i)
    return div
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append(i)

    if temp!=1:
        arr.append(temp)

    if arr==[]:
        arr.append(n)

    return arr

list1 = factorization(a)
list2 = factorization(b)
alllist = list1 + list2
if(list1 == [1] and list2 == [1]):
    print(1)
    exit()
ttmpansList = [x for x in alllist if alllist.count(x) > 1]
ttmpansList.sort()
ans = []
tmpansList = list(set(ttmpansList))
print(len(tmpansList)+1)

