//N = 縦, M = 横
void updateNext(int (*current)[M], int (*next)[M], int N, int M)
{
    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <=M; j++){
            int cnt = 0;
            if(current[i-1][j-1] == ALIVE) cnt++; //左上
            if(current[i-1][j] == ALIVE) cnt++; //上
            if(current[i-1][j+1] == ALIVE) cnt++; //右上
            if(current[i][j-1] == ALIVE) cnt++; //左
            if(current[i][j+1] == ALIVE) cnt++; //右上
            if(current[i+1][j-1] == ALIVE) cnt++; //左下
            if(current[i+1][j] == ALIVE) cnt++; //下
            if(current[i+1][j+1] == ALIVE) cnt++; //右下

            if(cnt <= 1 || cnt >= 4) {
                next[i][j] = DEAD;
            } else if (current[i][j] == ALIVE && (cnt == 2 || cnt == 3)) {
                next[i][j] = ALIVE;
            } else if (current[i][j] == DEAD && cnt == 3) {
                next[i][j] = ALIVE;
            } else {
                next[i][j] = DEAD;
            }
    }
    return;
}