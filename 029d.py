n = input()
number = int(n)
length = len(n)

ans = 0
#最上位の桁数の時は別処理を書くようにする
for i in range(length):
    #print(ans)
    if(i == length - 1):
        if(n[0] == '1'):
            if(length == 1):
                ans = 1
            else:
                ans += int(n[1:]) + 1
        else:
            ans += (10**(i))
            
    else:
        tmp1 = (number % 10**(i+1))
        roap = (number // 10**(i+1))
        if(tmp1 > 0):
            ans += 10**i
        ans += roap * 10**i
        

print(ans)
wrong answer
-----------------------------

n = input()

number = int(n)
length = len(n)

ans = 0

for i in range(length):
    #最上位の場合の処理
    #該当する桁数の１が何回出てきているか（その桁以上を見て）
    ans += number // (10**(i+1))
    #該当する桁数が何回出て生きているか（その桁の数を見て）
    ans += number[:i] // (10**(i+1))

print(ans)