swich,lamp = map(int,input().split(' '))

swichOnLamp = []
for i in range(lamp):
    swichOnLamp.append(list(map(int,input().split(' ')))[1:])
    
onlamp = list(map(int,input().split(' ')))
pattern = 2**swich
ans = 0
#print(swichOnLamp)
for i in range(pattern):
    #print(i)
    bitnum = list(reversed(list(format(i, 'b'))))
    tmponlamp = []
    #print(bitnum)
    lampArray = []
    for index,s in enumerate(bitnum):
        if(s=='1'):
            tmponlamp.append(index+1)
    #print(tmponlamp)
    for index,l in enumerate(swichOnLamp):
        cnt = 0
        #print(index,l,tmponlamp)
        for ll in l:
            if(ll in tmponlamp):
                cnt += 1
        if(cnt % 2 == onlamp[index]):
            lampArray.append(index)
    #print(tmponlamp)
    if(len(lampArray) == lamp):
        #print(tmponlamp)
        ans+=1
print(ans)