n,k = map(int, input().split(' '))
tmp = 0
#Kが一回も現れないとき

#ｋが一回現れるとき
tmp += (k-1)*(n-k) * 6
#kが二回現れる時
tmp += (n-1) * 3
#kが三回現れるとき
tmp += 1

ans = tmp / n**3
print(ans)