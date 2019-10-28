# coding: utf-8
# Your code here!


def calcScore(board, vertical, horizon):
    tmpsum = 0
    for i in range(2):
        for j in range(3):
            if board[i+1][j] == board[i][j]:
                tmpsum += vertical[i][j]
    for i in range(3):
        for j in range(2):
            if board[i][j+1] == board[i][j]:
                tmpsum += horizon[i][j]
    return tmpsum

def marubatugame(board, num, vertical, horizon, memo):
    if str(board) in memo:
        return memo[str(board)]
    
    if num == 10:
        return calcScore(board, vertical, horizon)
        
    bs1 = 0
    bs2 = float('inf')
    
    for i in range(3):
        for j in range(3):
            if board[i][j] is not None:continue
            board[i][j] = num % 2
            s = marubatugame(board, num+1, vertical, horizon, memo)
            board[i][j] = None
            bs1 = max(bs1, s)
            bs2 = min(bs2, s)
    ret = bs1 if num%2 else bs2
    memo[str(board)]  = ret
    return ret



vertical = []
horizon = []
for _ in range(2):
    vertical.append(list(map(int,input().split(' '))))
for _ in range(3):
    horizon.append(list(map(int,input().split(' '))))
total = sum([sum(i) for i in vertical]) + sum([sum(j) for j in horizon])
board = [[None for _ in range(3)] for _ in range(3)]
memo = {}
ans = marubatugame(board, 1, vertical, horizon, memo)
print(ans)
print(total - ans)