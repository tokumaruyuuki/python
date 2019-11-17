a,b,c,k = map(int,input().split(' '))
aa = list(map(int,input().split(' ')))
bb = list(map(int,input().split(' ')))
cc = list(map(int,input().split(' ')))
aa.sort(reverse=True)
bb.sort(reverse=True)
cc.sort(reverse=True)
aabb=[]
for i in aa:
    for j in bb:
        aabb.append(i+j)
aabb.sort(reverse=True)
#print(len(aabb))
combine_array = aabb[:k]
#print(len(combine_array))
ans_array = []
for i in combine_array:
    for j in cc[:k]:
        ans_array.append(i+j)
ans_array.sort(reverse=True)
#print(ans_array)
for i in range(k):
    print(ans_array[i])

PYPYで通した。