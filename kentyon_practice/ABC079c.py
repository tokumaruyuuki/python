# coding: utf-8
# Your code here!

n = list(map(int, list(input())))
for i in range(2**3):
    bit = format(i, "03b")
    tmp = n[0]
    for b in range(3):
        if bit[b] == "1":
            tmp += n[b+1]
        else:
            tmp -= n[b+1]
    if tmp == 7:
        ans = list(map(str,n))
        for b in range(3):
            if bit[b] == "1":
                ans.insert(2*b+1, "+")
            else:
                ans.insert(2*b+1, "-")
        print("".join(ans) + "=7")
        exit()