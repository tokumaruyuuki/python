height, vertical = map(int, input().split(" "))

campusList = []
for i in range(height):
    tmp = input()
    campusList.append(list(tmp))

ansFlag = 0

for h in range(height):
    for w in range(vertical):
        if(campusList[h][w] == "#"):
            upheight = h + 1 if h < height - 1 else h
            downheight = h - 1 if h >= 0 else h
            left = w - 1 if w >= 0 else w 
            right = w + 1 if w < vertical - 1 else w
            if(campusList[upheight][w] == "." and campusList[downheight][w] == "." and campusList[h][left] == "." and campusList[h][right] == "."):
                ansFlag = 1
                break

if(ansFlag == 1):
    print("No")
else:
    print("Yes")
            