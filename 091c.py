dots = int(input())
red = []
blue = []

for i in range(dots):
    x,y = map(int, input().split(" "))
    red.append([x,y])
for i in range(dots):
    x,y = map(int, input().split(" "))
    blue.append([x,y])
#x座標の次にyでソートする
red2 = list(reversed(sorted(red,key=lambda x:x[1]))) 
blue2 = sorted(blue,key=lambda x:(x[0],x[1]))
#print(blue2)
#print(red2)
ans = 0

for b in blue2:
    #print(b)
    for i, r in enumerate(red2):
        #print(r)
        if(b[0] > r[0] and b[1] > r[1]):
            ans += 1
            red2.pop(i)
            break

print(ans)