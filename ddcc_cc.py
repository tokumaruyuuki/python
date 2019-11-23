tate,yoko,cakes = map(int,input().split())
array = [[] for _ in  range(tate)]
#print(array)
for i in range(tate):
    array[i].append(list(input()))
ans_array = [[[] for _ in range(yoko)] for i in range(tate)]
cnt = 0
#print(array)
for t in range(tate):
    now = False
    for y in range(yoko):
        #print(t,y)
        if(array[t][0][y] == '#' and not now):
            cnt += 1
            for i in range(y+1):
                ans_array[t][i] = cnt
            now = True
        elif(array[t][0][y] == '#' and now):
            cnt +=1
            ans_array[t][y] = cnt
        elif(now):
            ans_array[t][y] = cnt
        #print(ans_array[t])
for t in range(tate):
    for y in range(yoko):
        if(ans_array[t][y] == []):
            if(t==0):
                for i in range(tate):
                    if(ans_array[i][y] != []):
                        ans_array[t][y] = ans_array[i][y]
                        break
            else:
                ans_array[t][y] = ans_array[t-1][y]
 
#print(ans_array[0])
for ans in ans_array:
    tmp = list(map(str ,ans))
    print(" ".join(tmp))