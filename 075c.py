import copy
 
n, m = map(int, input().split(" "))
bridge = [[0 for _ in range(n)] for _ in range(n)]
bridgePair = []
for _ in range(m):
    a,b = map(int, input().split(" "))
    bridgePair.append([a,b])
    bridge[a-1][b-1] = 1
    bridge[b-1][a-1] = 1

def dfs(i):
    visitArray[i-1] = 1
    for j in range(1,n+1):
        if(tmpArray[i-1][j-1] == 1 and visitArray[j-1] == 0):
            dfs(j)
    return

ans = 0
for pair in bridgePair:
    a,b = pair
    tmpArray = copy.deepcopy(bridge)
    tmpArray[a-1][b-1] = 0
    tmpArray[b-1][a-1] = 0
    visitArray = [0] * n
    dfs(1)
    if( 0 in visitArray):
        ans += 1
        
print(ans)