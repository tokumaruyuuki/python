N,M = map(int, input().split())
boards = [None] * N
passed = [[False] * M for i in range(N)]
for i in range(N):
    boards[i] = list(input())
for i in range(N):
    for j in range(M):
        if boards[i][j] == '#':
            if ((i < N - 1 and boards[i+1][j] == '#') or 
                (i >= 1 and boards [i-1][j] == '#') or 
                (j < M - 1 and boards[i][j+1] == '#') or
                (j >= 1 and boards[i][j-1] == '#')):
                    continue
            else:
                print('No')
                exit()
print('Yes')