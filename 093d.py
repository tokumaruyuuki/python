q = int(input())
 
def search(a,b):
    left, right = a-1,b * 2 - 1
    limit = a * b - 1
    while right - left > 1:
        center = (right + left) // 2
        max_num = 0
        for i in range(max(center//2-10,1),center//2+11):
            max_num = max(max_num, i * (center + 1 - i))
        if max_num > limit:
            right = center
        else:
            left = center
    return(left-1)
            
for i in range(q):
    a,b = map(int, input().split())
    if a>b:
        a,b = b,a
    if a == b:
        print(2*(a-1))
        continue
    print(search(a,b))