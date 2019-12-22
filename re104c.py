D,G = map(int,input().split())
problems = []
for i in range(D):
    items, score = map(int, input().split())
    problems.append((items, score))

ans = float('inf')
for i in range(2**D):
    bit = list(format(i, '0' + str(D) + 'b'))
    po_cnt = 0
    pr_cnt = 0
    for ind in reversed(range(D)):
        if bit[ind] == '1':
            if problems[ind][0] * (ind+1) * 100  + po_cnt > G:
                need = (G - po_cnt) // ((ind+1) * 100) if (G - po_cnt) >= ((ind+1) * 100) else 1
                pr_cnt += need
                ans = min(ans, pr_cnt)
                break
            else:
                po_cnt += problems[ind][0] * (ind+1) * 100 + problems[ind][1]
                pr_cnt += problems[ind][0]
                if po_cnt >= G:
                    ans = min(ans, pr_cnt)
                    break
                
print(ans)