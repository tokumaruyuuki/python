from collections import deque
ll = [list(input()) for _ in range(10)]
cnt = 1
first = True
s1 = [1,0,-1,0]
s2 = [0,1,0,-1]
q = deque()
candidate = []
for i in range(10):
    for j in range(10):
        if ll[i][j] == "o":
            ll[i][j] = cnt
            cnt += 1
            q.append([i,j])
            while q:
                qq = q.popleft()
                a,b= qq[0], qq[1]
                for k in range(4):
                    ta = a + s1[k]
                    tb = b + s2[k]
                    if 0<= ta <= 9 and 0<= tb <= 9 and ll[ta][tb] == 'o':
                        ll[ta][tb] = ll[a][b]
                        q.append([ta,tb])
                    for kk in range(4):
                        tta = ta + s1[kk]
                        ttb = tb + s2[kk]
                        if 0<= tta <= 9 and 0<= ttb <= 9 and ll[tta][ttb] == 'o' and ll[ta][tb] == 'x':
                            candidate.append([ta , tb])
                            continue
if cnt >=3:
    cn = {i for i in range(1,cnt)}
    for i in range(len(candidate)):
        cc = []
        for j in range(4):
            ta = candidate[i][0] + s1[j]
            tb = candidate[i][1] + s2[j]
            if not 0<= ta <= 9 or not 0<= tb <= 9:
                continue
            if ll[ta][tb] != 'x':
                cc.append(ll[ta][tb])
        tp = set(cc)
        if tp == cn:
            print("YES")
            exit()
    else:
        print("NO")
        exit()
else:
    print('YES')