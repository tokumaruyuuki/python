h,w,d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(h)]
num_array = [0] * (h*w)
dis_array = [0] * (h*w)

for i in range(h):
    for j in range(w):
        #print(grid[i][j])
        num_array[grid[i][j] - 1] = [i+1,j+1]
#print(dis_array)
for i in reversed(range(h*w)):
    dis_array[i-d] += dis_array[i] + (abs(num_array[i][0] - num_array[i-d][0]) + abs(num_array[i][1] - num_array[i-d][1])) if i-d >= 0 else 0
#print(dis_array)

q = int(input())
for i in range(q):
    s,e = map(int, input().split())
    print(dis_array[s-1] - dis_array[e-1])