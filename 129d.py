ver,hor = map(int,input().split(' '))
lamp = []
right = [[0 for i in range(hor)] for i in range(ver)]
left =  [[0 for i in range(hor)] for i in range(ver)]
up =  [[0 for i in range(hor)] for i in range(ver)]
down =  [[0 for i in range(hor)] for i in range(ver)]
for i in range(ver):
    lamp.append(list(input()))
for tate in range(ver):
    for yoko in range(hor):
        if(lamp[tate][yoko] == '.'):
            left[tate][yoko] += left[tate][yoko-1] + 1 if(not yoko == 0) else 1
            up[tate][yoko] += up[tate-1][yoko] + 1 if(not tate == 0) else 1
            if(yoko >= 1 and lamp[tate][yoko-1] == '.'):
                right[tate][yoko] += right[tate][yoko-1] - 1
            else:
                cnt = 0
                for i in range(yoko,hor):
                    if(lamp[tate][i] == '.'):
                        cnt += 1
                    else:
                        break
                right[tate][yoko] = cnt
            if(tate >= 1 and lamp[tate-1][yoko] == '.'):
                down[tate][yoko] += down[tate-1][yoko] - 1
            else:
                cnt = 0
                for i in range(tate,ver):
                    if(lamp[i][yoko] == '.'):
                        cnt += 1
                    else:
                        break
                down[tate][yoko] = cnt
            
            
ans = 0
for i in range(ver):
    for j in range(hor):
        ans = max(ans,right[i][j] + left[i][j] + up[i][j] + down[i][j] - 3)
print(ans)


#pypyでAC pythonでTLE