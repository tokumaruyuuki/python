people,point,times = map(int,input().split(' '))
howtimes = [0]*people
for i in range(times):
    correct = int(input())
    howtimes[correct-1] += 1
for i in howtimes:
    if(i > times - point):
        print('Yes')
    else:
        print('No')