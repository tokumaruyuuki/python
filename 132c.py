n = int(input())
array = list(map(int, input().split(" ")))
flagArray = [0] * 10**5
for num in array:
    flagArray[num-1] += 1
ans1 = 0
flag = 100
tmp = 0
for i in range(10**5):
    tmp += flagArray[i]
    if(tmp == int(n/2) and flag != 1):
        ans1 = i
        flag = 1
        ##print("aaaaaaaaaa")
    elif(tmp > int(n/2)):
        #print("aaaa")
        if(flag == 1):
            print(i - ans1)
            flag = 0
            break
        else:
            print(0)
            flag = 0
            break
if(flag == 100):
    print(0)