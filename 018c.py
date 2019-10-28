# coding: utf-8
# Your code here!

tate,yoko,k =  map(int,input().split(' '))
board = []
for i in range(tate):
    board.append(input())
boardNum = [[[] for i in range(yoko)] for i in range(tate)] #上と下に何個〇があるか記憶する
for i in range(tate):
    for j in range(yoko):
        up = 0
        down = 0
        if (board[i][j] == 'o'):
            up += 1
            down += 1
            if (i >= 1):
                up += boardNum[i-1][j][0]
                if(board[i-1][j] == 'o'):
                    down += boardNum[i-1][j][1] - 1
                else:
                    for ii in range(i+1,tate):
                        if (board[ii][j] == 'o'):
                            down += 1
                        else:
                            break
            else:
                up = 1
                down = 1
                for ii in range(i+1,tate):
                    if (board[ii][j] == 'o'):
                        down += 1
                    else:
                        break
        boardNum[i][j] = [up,down]
