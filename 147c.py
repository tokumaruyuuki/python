n = int(input())
 
say = [[] for i in range(n)]
for i in range(n):
    times = int(input())
    for j in range(times):
        p, hone = map(int,input().split())
        say[i].append([p-1,hone])
ans = 0
for i in range(2**n):
    honest = [False] * n
    bin_str = format(i, '0' + str(n) + 'b')
    binstr = list(bin_str)
    tmp = 0
    for j in range(len(binstr)):
        if binstr[j] == '1':
            honest[j] = True
            tmp += 1
    #print(honest)
    flag = True
    for h in range(n):
        if(honest[h]):
            for ss in say[h]:
                if(ss[1] == 1):
                    if not honest[ss[0]]:
                        flag = False
                        break
                else:
                    if honest[ss[0]]:
                        flag = False
                        break
    else:
        ans = max(ans, tmp) if flag else ans
print(ans)