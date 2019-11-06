n=int(input())
array=list(map(int,input().split(' ')))

firstAns = sum(array) - 2*(sum(array[1::2]))
ans = [firstAns]
for i in range(1,n):
    ans.append(2*array[i-1] -ans[i-1])
ans = list(map(str,ans))

print(' '.join(ans))