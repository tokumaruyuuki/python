# coding: utf-8
# Your code here!

A,B,C,X,Y = map(int, input().split())
if A+B > C * 2 :
    ans = 0
    mi = min(X,Y)
    ma = max(X,Y)
    ans += mi * C * 2
    if ma == X:
        if A <= C * 2:
            ans += (ma - mi) * A
        else:
            ans += (ma - mi) * C *2
    else:
        if B <= C * 2:
            ans += (ma - mi) * B
        else:
            ans += (ma - mi) * C * 2
    print(ans)
else:
    ans = X * A + Y * B
    print(ans)