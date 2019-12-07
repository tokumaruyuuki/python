# coding: utf-8
# Your code here!

n = int(input())
array = list(map(int, input().split()))

evens = array[0::2]
odds = array[1::2]
cnt_evens = {}
cnt_odds = {}

for e in evens:
    if e in cnt_evens:
        cnt_evens[e] += 1
    else:
        cnt_evens[e] = 1
for o in odds:
    if o in cnt_odds:
        cnt_odds[o] += 1
    else:
        cnt_odds[o] = 1
cnt_evens = sorted(cnt_evens.items(), key = lambda x: -x[1])
cnt_odds = sorted(cnt_odds.items(), key = lambda x: -x[1])

evens_one = cnt_evens[0]
evens_two = cnt_evens[1] if len(cnt_evens) >=2 else False
odds_one = cnt_odds[0]
odds_two = cnt_odds[1] if len(cnt_odds) >= 2 else False
#print(cnt_evens,cnt_odds)
if(evens_one[0] == odds_one[0]):
    if(evens_two and odds_two):
        ans = min(n - evens_one[1] - odds_two[1], n - evens_two[1] - odds_one[1])
    elif(evens_two):
        ans = n - evens_two[1] - odds_one[1]
    elif(odds_two):
        ans = n - evens_one[1] - odds_two[1]
    else:
        ans = n // 2
else:
    ans = 0
    ans += n//2 - evens_one[1] if len(cnt_evens) >= 2 else 0
    ans += n//2 - odds_one[1] if len(cnt_odds) >= 2 else 0
print(ans)