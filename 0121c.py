#何がしたい？＝＞最小金額の値段を見つけて、そこから購入していきたい。
#注意点は？＝＞同じ金額は、一つにまとめておきたい。
#実装は？＝＞値段管理はリスト（”金額”：個数）でおけ

x = input().split(" ")
store = int(x[0])
need = int(x[1])
ans = 0
price = {}

for i in range(store):
    y = input().split(" ")
    pri = y[0]
    bottles = int(y[1])
    if pri in price.keys():
        price[pri] += bottles
    else:
        price[pri] = bottles
#print(price)
price_sort = sorted(price.items(), key=lambda x: x[0]) #安い順に並び変え
#print(price_sort)
for price_bottles in price_sort: #price_bottles=(価格、本数)になる
    if need == price_bottles[1]:
        ans += price_bottles[1] * int(price_bottles[0])
        break
    elif need > price_bottles[1]:
        ans += price_bottles[1] * int(price_bottles[0])
        need -= price_bottles[1]
    else:
        ans += need * int(price_bottles[0])
        break


print(ans)





x = input().split(" ")
store = int(x[0])
need = int(x[1])
ans = 0
price = {}

for i in range(store):
    y = input().split(" ")
    pri = y[0]
    bottles = int(y[1])
    if pri in price.keys():
        price[pri] += bottles
    else:
        price[pri] = bottles
#print(price)
price_sort = sorted(price.items(), key=lambda x: x[0])
#print(price_sort)
for i in range(store):
    price_bottles = price_sort[i]
    ans += int(price_bottles[0]) * price_bottles[1]
    need -= price_bottles[1]
    if need <= 0:
        ans -= -1 * need * int(price_bottles[0])
        break


print(ans)

##違う。なんか数学的なとっころが違う気がする

x = input().split(" ")
store = int(x[0])
need = int(x[1])
ans = 0
price = {}

for i in range(store):
    y = input().split(" ")
    pri = y[0]
    bottles = int(y[1])
    if pri in price.keys():
        price[pri] += bottles
    else:
        price[pri] = bottles
#print(price)
price_sort = sorted(price.items(), key=lambda x: x[0])
#print(price_sort)
for price_bottles in price_sort:
    if need == price_bottles[1]:
        ans += price_bottles[1] * int(price_bottles[0])
        break
    elif need > price_bottles[1]:
        ans += price_bottles[1] * int(price_bottles[0])
        need -= price_bottles[1]
    else:
        ans += need * int(price_bottles[0])
        break


print(ans)

##何がダメなのかよくわからない。