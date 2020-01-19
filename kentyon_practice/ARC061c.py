s = input()
n = len(s)
ans = 0
if n == 1:
    print(s)
    exit()
for i in range(2**(n-1)):
    bit = format(i, "0" + str(n-1) + "b")
    tmp= s[0]
    for j in range(len(bit)):
        if bit[j] == "1":
            ans += int(tmp) if tmp != "" else 0
            tmp = s[j+1]
        else:
            tmp += s[j+1]
    #print(bit)
    ans += int(tmp)
print(ans)