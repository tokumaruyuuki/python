import sys
input = sys.stdin.readline
 
n,m = map(int, input().split())
graph = [[] for _ in range(n)]
root = [i for i in range(n)]
heights = [0] * n
def find_root(a):
    ra = root[a]
    if ra == a:
        return a
    new_root = find_root(ra)
    root[a] = new_root
    return new_root
 
def merge(a,b):
    ra = find_root(a)
    rb = find_root(b)
    if ra != rb:
        if heights[ra] >= heights[rb]:
            heights[ra] += 1
            root[rb] = ra
        else:
            heights[rb] += 1
            root[ra] = rb
 
 
for i in range(m):
    l,r,d = map(int,input().split())
    graph[l-1].append([r-1,d])
    graph[r-1].append([l-1,-d])
    merge(l-1,r-1)
 
 
for i in range(n):
    find_root(i)
    
dist = [None] * n
for i in set(root):
    stack = [i]
    dist[i] = 0
    while stack:
        next_x = stack.pop()
        for next_y, d in graph[next_x]:
            if dist[next_y] is None:
                dist[next_y] = dist[next_x] + d
                stack.append(next_y)
            elif dist[next_y] != dist[next_x] + d:
                print("No")
                exit()
print("Yes")