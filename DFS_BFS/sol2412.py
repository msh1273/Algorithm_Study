import sys
from collections import deque
# n : 암벽에 파인 홈의 개수, T : 도달할 높이
n, T = map(int, sys.stdin.readline().rstrip().split())

dot = set()
for i in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    dot.add((x,y))

queue = deque()
queue.append([0, 0, 0])
flag = False
while queue:
    x, y, count = queue.popleft()
    if y == T:
        flag =True
        break
    for i in range(-2, 3):
        for j in range(-2, 3):
            nx = x + i
            ny = y + j
            if (nx, ny) in dot:
                queue.append([nx, ny, count + 1])
                dot.remove((nx, ny))
                
if flag:
    print(count)
else:
    print(-1)
