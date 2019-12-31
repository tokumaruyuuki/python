N,C = map(int, input().split())
colors = []
for i in range(C):
    colors.append(list(map(int, input().split())))
boards = []
for i in range(N):
    boards.append(list(map(int, input().split())))
dp = [[0] * C for i in range(3)]

for i in range(N):
    for j in range(N):
        for c in range(C):
            dp[(i+j)%3][c] += colors[boards[i][j]-1][c]

ans = float('inf')

for c1 in range(C):
    for c2 in range(C):
        for c3 in range(C):
            if c1 == c2 or c1 == c3 or c2 == c3:
                continue
            ans = min(ans,dp[0][c1] + dp[1][c2] + dp[2][c3])
print(ans)