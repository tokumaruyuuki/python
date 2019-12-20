cities, trains, query = map(int, input().split())
dp=[[0] * cities for _ in range(cities)]
for t in range(trains):
    s, e = map(int, input().split())
    dp[s-1][e-1] += 1

for x in range(cities):
    for y in range(x, cities-1):
        dp[x][y+1] += dp[x][y]

for x in range(cities):
    for y in range(x, 0, -1):
        dp[y-1][x] += dp[y][x]
#print(dp)
for q in range(query):
    s,e = map(int,input().split())
    print(dp[s-1][e-1])