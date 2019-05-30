times = int(input())

memberDict = {}
maxnum = 1
ans = ""
for i in range(times):
    tmp = input()
    if(tmp in memberDict.keys()):
        memberDict[tmp] += 1
    else:
        memberDict[tmp] = 1
    if(maxnum <= memberDict[tmp]):
        maxnum = memberDict[tmp]
        ans = tmp
        
print(ans)