cards, gate = map(int,input().split(' '))
cardsArray = [0] * (cards+1)
ans = 0
for i in range(gate):
    start,end = map(int,input().split(' '))
    cardsArray[start-1] += 1
    cardsArray[end] -= 1
for i in range(len(cardsArray)):
    if(i>0):cardsArray[i] += cardsArray[i-1]
    if(cardsArray[i] == gate):
        ans += 1
print(ans)