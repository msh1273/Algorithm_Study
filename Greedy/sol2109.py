import sys
import heapq

n = int(sys.stdin.readline())
pd_list = []
result = 0
for i in range(n):
    pd_list.append(list(map(int, sys.stdin.readline().split())))

pd_list.sort(key=lambda x : x[1])   #d기준으로 오름차순 정렬
p_list = []
for i in pd_list:
    heapq.heappush(p_list, i[0])
    if len(p_list) > i[1]:
        heapq.heappop(p_list)
        
print(sum(p_list))