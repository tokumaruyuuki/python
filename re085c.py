# coding: utf-8
# Your code here!
n, y = map(int, input().split())
a,b,c = 0,0,0
c = y // 1000

for nine in range(2001):
    for four in range(2001):
        cards = c - (10*nine + 5*four)
        #print(cards, nine,four)
        if cards < 0:
            continue
        if cards + nine + four == n and 1000*cards + 10000*nine + 5000*four == y:
            print(nine, four,cards)
            exit()
else:
    print(-1,-1,-1)