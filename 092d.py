a,b = map(int, input().split())
a-=1
b-=1
N = 50
W = 100
grid = [['.'] * W for _ in range(N)] # 黒にする
grid2 = [['#'] * W for _ in range(N)] # 白にする
#print(grid)
for i in range(1,N,2):
    for j in range(0,W,2):
        if b == 0:
            break
        grid[i][j] = "#"
        b -= 1
for i in range(1,N,2):
    for j in range(0,W,2):
        if a == 0:
            break
        grid2[i][j] = "."
        a -= 1
print(W,W)
for i in range(N):
    print("".join(grid[i]))
for i in range(N):
    print("".join(grid2[i]))