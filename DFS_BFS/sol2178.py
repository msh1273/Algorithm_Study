import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())

#미로 초기화
maze = [[0 for _ in range(m)] for _ in range(n) ]

#방문 기록
visited = [0 for _ in range(m) for _ in range(n)]

# 미로 입력
for i in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip()))
    for j in range(m):
        if temp[j] == 1:
            maze[i][j] = 1


def bfs(x, y):
    # 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        #갈 수 있는 방향 찾기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #갈 수 있는 곳이라면
            if 0 <= nx < n and  0 <= ny < m and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    return maze[n-1][m-1]

print(bfs(0, 0))

