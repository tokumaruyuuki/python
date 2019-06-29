string = input()
 
dic = {}
 
for i in string:
    if(i in dic):
        dic[i] += 1
    else:
        dic[i] = 1
 
flag = 0 if(len(dic) == 2) else 1
for v in dic.values():
    if(v != 2):
        flag = 1
 
if(flag == 0):
    print("Yes")
else:
    print("No")