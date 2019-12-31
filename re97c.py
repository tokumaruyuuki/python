S = input()
K = int(input())
candidate = []
sp_s = sorted(set(list(S)))
for s in sp_s:
    flag = True
    for i in range(len(S)):
        if S[i] == s:
            if flag:
                candidate.append(s)
                flag = False
            str_array = s
            for j in range(i+1,i+K+1):
                if j >= len(S):
                    continue
                str_array += S[j]
                if str_array not in candidate:
                    candidate.append(str_array)
    if len(candidate) > K:
        break
#print(candidate)
tmp = sorted(candidate)
print(tmp[K-1])