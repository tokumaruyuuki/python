def findRoot(index1, index2, root = []):
    #print(root)
    for i in range(1,top):
        if(array[index2][i] == 1 and i not in root and i != 0):
            root.append(i)
            findRoot(index2, i, root)
    if(len(root) == top-1):
        return True
    else:
        return False


top, hen = map(int, input().split(" "))

array = [[0 for i in range(top)] for j in range(top)]

for i in range(hen):
    a,b = map(int, input().split(" "))
    array[b-1][a-1] = 1
    array[a-1][b-1] = 1

#print(array)
ans = 0
for i in range(1,top):
    if(array[0][i] == 1):
        flag = findRoot(0, i,[i])
        #print(flag)
        if(flag):
            ans += 1

print(ans)

----------------------------------------------
