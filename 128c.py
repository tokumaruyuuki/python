card, gate = map(int, input().split(" "))
cardArray = []
first1, first2 = map(int, input().split(" "))
for i in range(first1,first2+1):
    cardArray.append(i)
    

for i in range(gate-1):
    start, end = map(int, input().split(" "))
    for i in cardArray:
        if(len(cardArray) == 0):
            break
        if(start > i or i > end ):
            cardArray.remove(i)

print(len(cardArray))
-------------------------------------------
card, gate = map(int, input().split(" "))
cardArray = [0] * (card + 1)

for i in range(gate):
    start, end = map(int, input().split(" "))
    ##print(start)
    cardArray[start-1] += 1
    cardArray[end] -= 1
nowstatus = 0
presatus = 0
ans = 0
##print(cardArray)
for i in range(card):
    nowstatus += cardArray[i]
    if(presatus > nowstatus):
        break
    elif(nowstatus >= gate):
        ans += 1
    presatus = nowstatus

print(ans)


----------------------

N,M = map(int,input().split())
 
# kの値は特に必要ないので最初から取得しない
S=[list(map(int,input().split()))[1:] for i in range(M)]
p = list(map(int,input().split()))
ans = 0
for i in range(1<<N): #スイッチのオンオフ状態
    
    for m in range(M):  #電球の状態 
        count = 0
        for s in S[m]:
            if i & (1<<(s-1)) != 0:
                count += 1
                # 電球に対するスイッチのonの数を取得する
        if count%2 != p[m]:
            break
    else:
        # あるスイッチのパターンに対して各電球がOKだったらカウントする
        ans +=1
print(ans)