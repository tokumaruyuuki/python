import heapq

goods, coopon = map(int,input().split(' '))
array = list(map(int,input().split(' ')))
for i in range(len(array)):
    array[i] *= -1
heapq.heapify(array)
while coopon > 0:
    tmp = heapq.heappop(array)
    tmp *= -1
    tmp //= 2
    tmp *= -1
    heapq.heappush(array,tmp)
    coopon-=1
#print(array)
print(sum(array) * -1)