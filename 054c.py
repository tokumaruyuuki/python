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
import copy
 
n,m = map(int ,input().split(" "))
 
bridge = [[0 for i in range(n)] for i in range(n)]
 
ans = 0
 
def findRoot(i):
    global ans
    if(0 not in tmpArray):
        ans += 1
    for j in range(1, n):
        if(tmpArray[j] == 0 and bridge[i][j] == 1):
            tmpArray[j] = 1
            findRoot(j)
            tmpArray[j] = 0
 
for i in range(m):
    a,b = map(int, input().split(" "))
    bridge[a-1][b-1] = 1
    bridge[b-1][a-1] = 1
visitArray = [0] * n
for i in range(1,n):
    tmpArray = copy.deepcopy(visitArray)
    if(bridge[0][i] == 1):
        tmpArray[0] = 1
        tmpArray[i] = 1
        findRoot(i)
 
 
print(ans)