N = int(input())
array = list(map(int, input().split()))

p,q,r,s = 0, array[0], sum(array[1:3]), sum(array[3:])
ans = float('inf')
left, right = 0, 2
for c in range(1, N-2):
    p += array[c];r -= array[c]
    while left < c-1:
        next_num = array[left+1]
        if abs((p - next_num) - (q + next_num)) <= abs(p - q):
            left += 1
            p -= next_num
            q += next_num
        else:
            break
    
    while right < N - 2:
        next_num = array[right+1]
        if abs((s - next_num) - (r + next_num)) <= abs(s - r):
            right += 1
            r += next_num
            s -= next_num
        else:
            break
    
    res = sorted([p,q,r,s])

    ans = min(ans, res[-1] - res[0])

print(ans)
    