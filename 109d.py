tate, yoko = map(int, input().split())
array = [[] for _ in range(tate)]
for i in range(tate):
    array[i] = list(map(int,input().split()))
ans = 0
ans_list = []
even_odd = 0
while even_odd != yoko :
    if even_odd % 2 == 0:
        for t in range(tate):
            if array[t][even_odd] % 2 == 1:
                ans += 1
                if t == tate - 1 and even_odd + 1 <= yoko-1:
                    array[t][even_odd] -= 1
                    array[t][even_odd+1] += 1
                    ans_list.append([str(t+1),str(even_odd+1),str(t+1),str(even_odd+2)])
                elif t < tate - 1 :
                    array[t][even_odd] -= 1
                    array[t+1][even_odd] += 1
                    ans_list.append([str(t+1),str(even_odd+1),str(t+2),str(even_odd+1)])
        else:
            even_odd += 1
    else:
        for t in reversed(range(tate)):
            if array[t][even_odd] % 2 == 1:
                ans += 1
                if t == 0 and even_odd + 1 <= yoko-1:
                    array[t][even_odd] -= 1
                    array[t][even_odd+1] += 1
                    ans_list.append([str(t+1),str(even_odd+1),str(t+1),str(even_odd+2)])
                elif t > 0:
                    array[t][even_odd] -= 1
                    array[t-1][even_odd] += 1
                    ans_list.append([str(t+1),str(even_odd+1),str(t),str(even_odd+1)])
        else:
            even_odd += 1
        
print(len(ans_list))
for ll in ans_list:
    print(' '.join(ll))

