import itertools
n = int(input())
k = int(input())
ll = [input() for _ in range(n)]
tmp_l = []
for i in itertools.permutations(ll,k):
    tmp_str = "".join(i)
    if tmp_str not in tmp_l:
        tmp_l.append(tmp_str)
print(len(tmp_l))