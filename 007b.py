alpha = input()
array = ["a","b","c","d","e","f","g","h","i","j","k","l","n","m","o","p","q","r","s","t","u","v","w","x","y","z"]
if(len(alpha) >1):
    alphaArray = list(alpha)
    alphaArray.pop(-1)
    print("".join(alphaArray))
else:
    indexNum = array.index(alpha)
    if(indexNum == 0):
        print(-1)
    else:
        print(array[indexNum-1])