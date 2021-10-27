import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
line = int(sys.stdin.readline().rstrip())

graph = [[0]*(n+1) for i in range(n+1)]

for i in range(line):
    c1, c2 = map(int, sys.stdin.readline().split())
    graph[c1][c2] = graph[c2][c1] = 1

visited = [0]*(n+1)

def bfs(v):
    deq = deque()
    deq.append(v)
    visited[v] = 1
    while deq:
        temp = deq.popleft()
        for i in range(1, n+1):
            if graph[temp][i] == 1 and visited[i] == 0:
                deq.append(i)
                visited[i] = 1

bfs(1)
visited = visited[2:]

count = 0

for i in visited:
    if i == 1:
        count+=1

print(count)