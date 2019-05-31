inputnum = input()
num1 = int(inputnum[0]) * 10
num2 = int(inputnum[1])
num3 = int(inputnum[2]) * 10
num4 = int(inputnum[3])
prenum = num1 + num2
brenum = num3 + num4
if(prenum == 0):
    if(brenum == 0):
        print("NA")
    elif(brenum > 12):
        print("NA")
    else:
        print("YYMM")
elif(brenum == 0):
    if(prenum == 0):
        print("NA")
    elif(prenum > 12):
        print("NA")
    else:
        print("MMYY")
elif(prenum <= 12 and brenum <= 12):
    print("AMBIGUOUS")
elif(prenum > 12):
    if(brenum <= 12):
        print("YYMM")
    else:
        print("NA")
elif(prenum <= 12):
    print("MMYY")
elif(brenum > 12):
    if(prenum <= 12):
        print("MMYY")
    else:
        print("NA")
elif(brenum <= 12):
    print("YYMM")