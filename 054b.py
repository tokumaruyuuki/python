N, M = map(int, input().split())
 
A = []
for i in range(N):
    A.append(list(input()))
 
B = []
for i in range(M):
    B.append(list(input()))
 
exist = False
 
for i in range(N - M + 1):
    for j in range(N - M + 1):
        flag = True
        for k in range(M):
            for l in range(M):
                if B[k][l] != A[i + k][j + l]:
                    flag = False
                    break
        if flag:
            exist = True
if exist:
    print("Yes")
else:
    print("No")