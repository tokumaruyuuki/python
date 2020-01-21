# coding: utf-8
# Your code here!
d,g = map(int, input().split())
prob = []
ans = float('inf')
for i in range(d):
    a,b = map(int, input().split())
    prob.append([100*(i+1),a,b])
prob.reverse()
for i in range(2**d):
    bit = format(i, "0" + str(d) + "b")
    solves = 0
    points = 0
    for b in range(d):
        #print(bit, b)
        if bit[b] == "1":
            #print(prob[b][0] , prob[b][1], points, bit)
            if points + prob[b][0] * prob[b][1] >= g:
                tmp =  (g - points) // prob[b][0] if (g - points) % prob[b][0]  == 0 else (g - points) // prob[b][0] + 1
                solves += tmp
                points += g
                break
            else:
                solves += prob[b][1]
                points += prob[b][0] * prob[b][1] + prob[b][2]
                if points >= g:
                    break
    if points >= g:
        ans = min(solves, ans)

print(ans)