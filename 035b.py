string = input()
strindList = list(string)
lenght = len(strindList)
tmp = int(input())
horizon = 0
vertical = 0
sub = 0
if(tmp == 1):
    for i in range(lenght):
        if(strindList[i] == "U"):
            vertical += 1
        elif(strindList[i] == "D"):
            vertical -= 1
        elif(strindList[i] == "R"):
            horizon -= 1
        elif(strindList[i] == "L"):
            horizon += 1
        elif(strindList[i] == "?"):
            sub += 1
    print(abs(horizon) + abs(vertical) + sub)
else:
    for i in range(lenght):
        if(strindList[i] == "U"):
            vertical += 1
        elif(strindList[i] == "D"):
            vertical -= 1
        elif(strindList[i] == "R"):
            horizon -= 1
        elif(strindList[i] == "L"):
            horizon += 1
        elif(strindList[i] == "?"):
            sub += 1
    if(abs(horizon) + abs(vertical) - sub >= 0):
        print(abs(horizon) + abs(vertical) - sub)
    else:
        aaa = abs(abs(horizon) + abs(vertical) - sub)
        if(aaa % 2 == 0):
            print(0)
        else:
            print(1)
    