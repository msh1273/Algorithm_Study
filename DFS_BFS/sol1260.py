from collections import deque
import sys
n, m, v = map(int, sys.stdin.readline().split())
matrix = [[0] * (n+1) for i in range(n+1)]
visited = [0] * (n+1)
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    matrix[a][b] = matrix[b][a] = 1

def dfs(v):
    print(v, end=' ')
    visited[v] = 1
    for i in range(1, n+1):
        if visited[i] == 0 and matrix[v][i] == 1:
            dfs(i)

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = 1

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if matrix[v][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i]=1


dfs(v)
print()
visited = [0] * (n+1)
bfs(v)