import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

queue = deque()
queue.extend([i for i in range(1, n+1)])

while len(queue) != 1:
    queue.popleft()
    queue.rotate(-1)

print(queue[0])