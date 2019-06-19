length = int(input())

times = 1
stringLen = ""
array = ["a", "b", "c"]
ansArray = ["a", "b", "c"]
while times < length:
    tmp = []
    for i in range(len(ansArray)):
        for j in range(3):
            tmp.append(ansArray[i] + array[j])
    
    ansArray += tmp
    times += 1

for i in range(len(ansArray)):
    if(len(ansArray[i]) == length):
        print(ansArray[i])