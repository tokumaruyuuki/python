N, K = map(int, input().split())
array = list(map(int, input().split()))
update_cnt = K - 1
N -= 1
if N % update_cnt != 0:
    ans = N //update_cnt + 1
else:
    ans = N // update_cnt
print(ans)