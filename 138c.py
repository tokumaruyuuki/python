import heapq
n = int(input())
array = list(map(int, input().split(' ')))
ans = 0
heap = []
for i in array:
    heapq.heappush(heap, i)

for i in range(n-1):
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    tnp = (a + b) / 2
    heapq.heappush(heap,tnp)
print(heap[0])