# coding: utf-8
# Your code here!

import bisect

n = int(input())
side  = list(map(int,input().split(' ')))
side.sort()
ans = 0

for i in reversed(range(2,n)):
    for j in reversed(range(1,i)):
        index = bisect.bisect_right(side,side[i] - side[j])
        if(index < j):
            ans += j -index
    
print(ans)