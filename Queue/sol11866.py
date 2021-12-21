import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int , input().rstrip().split())

yo = deque()
yo.extend([str(i) for i in range(1, n+1)])

answer = []
while yo:
    yo.rotate(-(k-1))
    answer.append(yo.popleft())

answer = ', '.join(answer)
print(f"<{answer}>")