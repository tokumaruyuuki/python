time = int(input())
takoyaki = int(input())
takoArray = list(map(int, input().split(" ")))
Istako = [False] * 100
customer = int(input())
customerArray = list(map(int, input().split(" ")))

def takoyaki(customerTime, time):
    start = 0 if(customerTime-1-time <= 0) else customerTime-1-time
    end = 100 if(customerTime+time >= 100) else customerTime+time
    #print(start)
    #print(end)
    for tako in range(start, end):
        if(Istako[tako] == True):
            Istako[tako] = False
            return True
    else:
        return False

for i in range(len(takoArray)):
    Istako[takoArray[i]-1] = True
ansFlag = True
for i in range(customer):
    canTake = takoyaki(customerArray[i],time)
    if(canTake):
        continue
    else:
        ansFlag = False
        break

if(ansFlag):
    print("yes")
else:
    print("no")
---------------------------------------------

