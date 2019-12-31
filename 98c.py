N = int(input())
array = input()

w_array = [0] * N
e_array = [0] * N

for i in range(N):
    w_array[i] = w_array[i-1]
    e_array[i] = e_array[i-1]
    if array[i] == 'W':
        w_array[i] += 1
    else:
        e_array[i] += 1
    

ans = float('inf')
#print(e_array)
for i in range(N):
    cnt = 0
    if i > 0:
        cnt += w_array[i-1]
    if i < N-1:
        cnt += e_array[-1] - e_array[i]
    ans = min(ans, cnt)
print(ans)