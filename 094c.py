number = int(input())
originlist = list(map(int, input().split(" ")))
subList = []
for i in originlist:
    subList.append(i)
subList.sort()
for i in range(number):
    subList.remove(originlist[i])
    print(subList[int(number/2) - 1])
    subList.append(originlist[i])
    subList.sort()

------------------------------------------------
