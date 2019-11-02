mass = int(input())
array = list(map(int,input().split(' ')))

ans = 0
nowtimes = 0
minhights = array[0]
for i in range(1,mass):
    if(array[i]<=minhights):
        nowtimes += 1
        minhights = array[i]
    else:
        ans = max(ans, nowtimes)
        nowtimes = 0
        minhights = array[i]
ans = max(ans,nowtimes)
print(ans)