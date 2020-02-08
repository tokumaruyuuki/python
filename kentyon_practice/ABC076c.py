st = list(input())
samp_l = list(input())
rev_st = list(reversed(st))
rev_samp = list(reversed(samp_l))
if len(st) < len(samp_l) :
    print("UNRESTORABLE")
    exit()
for i in range(len(st)):
    if rev_samp[0] == rev_st[i] or rev_st[i] == "?":
        for j in range(len(rev_samp)):
            if i + j >= len(st):
                break
            if rev_samp[j] == rev_st[i+j] or rev_st[i+j] == "?":
                continue
            else:
                break
        else:
            ans = rev_st[:i] + rev_samp + rev_st[i+j+1:] if i+j+1 <= len(st)-1 else rev_st[:i] + rev_samp + rev_st[i+j+1:]
            break
try:
    ans 
    for i in range(len(ans)):
        if ans[i] == '?':
            ans[i] = 'a'
    print("".join(list(reversed(ans))))
except NameError:
    print("UNRESTORABLE")