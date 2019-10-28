import heapq
 
n = int(input())
start, goal = map(int, input().split())
m = int(input())
routes = [[] for _ in range(n+1)]
 
for _ in range(m):
    x, y = map(int, input().split())
    routes[x].append(y)
    routes[y].append(x)
 
min_path = [0] * (n+1)
min_path[start] = 1
min_distance = [float('INF')]*(n+1)
min_distance[start] = 0
todo = [[0, start]]
heapq.heapify(todo)
 
while todo:
    distance, town = heapq.heappop(todo)
    for next_town in routes[town]:
        if min_distance[next_town] > distance + 1:
            min_distance[next_town] = distance + 1
            min_path[next_town] = min_path[town]
            
        elif min_distance[next_town] == distance + 1:
            min_path[next_town] += min_path[town]
            min_path[next_town] %= 1000000007
            continue
 
        else:
            continue
        heapq.heappush(todo, [distance + 1, next_town])
        
print(min_path[goal])