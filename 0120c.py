#尺取り法で行ける

#何がしたい？＝＞"0""1"のペアを探していく
#どのように？＝＞頭から見ていく。
#注意点＝＞交互になっているときは素直にやればよい。でも００１１のようなときにどうするか
#実装
"""
まず、最初の要素を見ていく。
もし、何も保留していなければ
    隣が違う数字であれば、その場で取り除いていく。

    保留してある場合
    異なる数字に当たるまで探していく
"""


x = input()
number = list(x)
left = ""
left_len = 0
ans = 0
now_left = ""
for i in range(len(number)):
    if now_left == "":
        if left_len == 0:
            now_left = number[i]
            left = number[i]
            left_len += 1
        else:
            if left != number[i]:
                ans += 2
                left_len -= 1
            else:
                left_len += 1
    else:
        if now_left != number[i]:
            ans += 2
            now_left = ""
            left_len -= 1
        else:
            left_len += 1

print(ans)

#accepted.