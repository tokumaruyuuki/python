sign, points = map(int,input().split())
array = list(map(int, input().split()))
array.sort()
if(sign >= points):
    print(0)
else:
    distances = [array[i] - array[i-1] for i in range(1,points)]
    distances.sort()
    ans = distances[:points - sign]
    print(sum(ans))