# coding: utf-8
# Your code here!

stores, need_bottle = map(int,input().split(' '))
stocks = {}
for i in range(stores):
    money,bottles = map(int,input().split(' '))
    if(money in stocks):
        stocks[money] += bottles
    else:
        stocks[money] = bottles
#print(stocks.items())
ans_list = sorted(stocks.items(), key=lambda x:x[0])
ans = 0
for m,b in ans_list:
    if(need_bottle<=b):
        ans+= need_bottle * m
        break
    else:
        ans+= b*m
        need_bottle -= b
print(ans)