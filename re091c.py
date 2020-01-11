N = int(input())
red = [list(map(int, input().split())) for i in range(N)]
blue = [list(map(int, input().split())) for i in range(N)]
ans = 0
red_sorted = sorted(red, key = lambda x : -x[0])
blue_sorted = sorted(blue, key = lambda x : x[0])
blue_used = [False] * N
#print(red_sorted)
#print(blue_sorted)
for i in range(N):
    blue_y = float("-inf")
    blue_index = None
    blue_candidate = []
    for j in range(N):
        if blue_used[j]:
            continue
        if red_sorted[i][0] < blue_sorted[j][0]:
            if (red_sorted[i][1] < blue_sorted[j][1]):
                blue_index = j
                blue_candidate.append((blue_index, blue_sorted[j][1]))
                #print(red_sorted[i][1], blue_sorted[j][1])
    if blue_index != None:
        blue_candidate = sorted(blue_candidate, key = lambda x : x[1])
        blue_used[blue_candidate[0][0]] = True
        ans += 1
print(ans)