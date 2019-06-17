yoko, tate, x, y = map(int, input().split(" "))
menseki = yoko * tate / 2
if(yoko == x * 2 and tate == y * 2):
    print(menseki, 1)
else:
    print(menseki, 0)