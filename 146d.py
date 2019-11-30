# coding: utf-8
# Your code here!
n = int(input())
#隣接する辺の色
ng_colors = [[] for _ in range(n)]
#つながっている辺
graph_list = [[] for _ in range(n)]
ans = 1
ans_list = []
for _ in range(n-1):
    a,b = map(int, input().split())
    tmp_ng_colors = list(set(ng_colors[a-1] + ng_colors[b-1]))
    k = 1
    while True: 
        if(len(tmp_ng_colors) >= ans):
            ans += 1
            k = ans
            break
        if(k in tmp_ng_colors):
            k += 1
        else:
            break
    ans_list.append(k)
    ng_colors[a-1].append(k)
    ng_colors[b-1].append(k)
    #print(tmp_ng_colors, k, ans, len(tmp_ng_colors))
print(ans)
for a in ans_list:
    print(a)
-------------------------------------
import sys
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for i in range(n)]
for i in range(n-1):
    a,b = map(int, input().split())
    a,b = a-1,b-1
    graph[a].append([b,i])
 
ans = [None]*(n-1)
def decide_colors(cur,color):
    cnt = 1
    for (to, j) in graph[cur]:
        if cnt == color:
            cnt += 1
        ans[j] = cnt
        decide_colors(to, cnt)
        cnt += 1
decide_colors(0, 0)
print(max(ans))
[print(a) for a in ans]