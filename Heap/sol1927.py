import sys
import heapq

N = int(sys.stdin.readline().rstrip())

heap = []
for i in range(N):
    a = int(sys.stdin.readline().rstrip())
    if a == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, a)
