import collections
import sys
from collections import deque
# n은 수빈위치, k는 동생위치
n, k = map(int, sys.stdin.readline().rstrip().split())

queue = deque()
queue.append(n)

visited = [0]*100001
visited[n] = 1
answer = 0
while queue:
    curPoint = queue.popleft()     #수빈이 현재위치
    if curPoint == k:
        answer = visited[curPoint] - 1
        break
    #move[0] == 앞으로 갈때, move[1] == 뒤로 갈때, move[2] == 순간이동
    move = [curPoint+1, curPoint-1, curPoint*2]

    #가는 경우는 3가지가 있다. (앞, 뒤, 순간이동)
    for i in move:
        if 0 <= i <= 100000 and visited[i] == 0:
            visited[i] = visited[curPoint] + 1
            queue.append(i)

print(answer)