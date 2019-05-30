#2の３６乗までを考える。（というのも、１０＊＊１２なら、この数字までが範囲だから。）
#なので、数字そのものを扱うのではなくこの値でうまく処理していきたい。
a,b = map(int, input().split(" "))

a_list=[0] * 37
b_list=[0] * 37
sub = 36
for i in range(37):
    sub2 = sub - i
    now_number = 2**sub2
    if a >= now_number:
        a_list[i] = 1
        a -= now_number
    if b >= now_number:
        b_list[i] = 1
        b -= now_number
    #print(now_number)
    #print(a)
    #print(b)
        
a_list.reverse()
b_list.reverse()
#print(a_list)
#print(b_list)
ans = [0] * 37
ans2 = 0
for i in range(37):
    if a_list[i] != b_list[i]:
        ans[i] = 1

for i in range(37):
    if ans[i] == 1:
        ans2 += 2**i

#print(ans)
print(ans2)
