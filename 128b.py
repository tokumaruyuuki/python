n = int(input())
list = []
for i in range(n):
    s,p = input().split()
    p = int(p)
    list.append([s,-p,i+1])
 
list.sort()
 
for s,p,i in list:
    print(i)