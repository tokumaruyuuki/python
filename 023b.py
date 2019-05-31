length = int(input())
stringa = input()
string = list(stringa)
if(length == 1):
    if(string[0] == "b"):
        print(0)
    else:
        print(-1)
elif(length % 2 == 0):
    print(-1)
else:
    centerIndex = int((length-1) / 2)
    if(string[centerIndex] != "b"):
        print(-1)
    else:
        times = int((length-1) / 2)
        array1 = string[0:centerIndex]
        array2 = string[centerIndex+1:length]
        status = times % 3
        flag = 0
        if(status == 0):
            for i in range(centerIndex-1):
                if(i % 3 == 0):
                    if(array1[i] != "b" or array2[-(i+1)] != "b"):
                        print(-1)
                        flag = 1
                        break
                elif(i % 3 == 1):
                    if(array1[i] != "c" or array2[-(i+1)] != "a"):
                        print(-1)
                        flag = 1
                        break
                elif(i % 3 == 2):
                    if(array1[i] != "a" or array2[-(i+1)] != "c"):
                        print(-1)
                        flag = 1
                        break
                    
        elif(status == 1):
            for i in range(centerIndex-1):
                if(i % 3 == 0):
                    if(array1[i] != "a" or array2[-(i+1)] != "c"):
                        print(-1)
                        flag = 1
                        break
                elif(i % 3 == 1):
                    if(array1[i] != "b" or array2[-(i+1)] != "b"):
                        print(-1)
                        flag = 1
                        break
                elif(i % 3 == 2):
                    if(array1[i] != "c" or array2[-(i+1)] != "a"):
                        print(-1)
                        flag = 1
                        break
        elif(status == 2):
            for i in range(centerIndex-1):
                if(i % 3 == 0):
                    if(array1[i] != "c" or array2[-(i+1)] != "a"):
                        print(-1)
                        flag = 1
                        break
                elif(i % 3 == 1):
                    if(array1[i] != "a" or array2[-(i+1)] != "c"):
                        print(-1)
                        flag = 1
                        break
                elif(i % 3 == 2):
                    if(array1[i] != "b" or array2[-(i+1)] != "b"):
                        print(-1)
                        flag = 1
                        break
        
        if(flag == 0):
            print(times)