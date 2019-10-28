# coding: utf-8
# Your code here!
from collections import deque
n = int(input())
cards = deque(['1','2','3','4','5','6'])
modd = n // 30
if (modd > 0 ):
    n -= 30 * modd
divfive = n // 5
modfive = n % 5
for i in range(divfive):
    tmp = cards.popleft()
    cards.append(tmp)

tmp = cards.popleft()
ans = list(cards)
ans.insert(modfive,tmp)
print(''.join(ans))