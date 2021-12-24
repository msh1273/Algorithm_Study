import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

links = []
for i in range(n):
    links.append(int(sys.stdin.readline().rstrip()))
links.sort()

start = 1
end = links[-1]

while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in links:
        count += i // mid
    if count >= k:  #라인이 목표 보다 더 많이 만들어 졌다는 것은 라인의 길이를 늘려야 한다.
        start = mid + 1
    else:
        end = mid -1

print( end)