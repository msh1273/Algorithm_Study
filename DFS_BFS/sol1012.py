import sys
from collections import deque

input = sys.stdin.readline

T = int(input().rstrip())

#상, 하, 좌, 우
mx =[0,0,-1,1]
my =[-1,1,0,0]



for i in range(T):
    #가로, 세로, 위치
    M, N, K = map(int, input().rstrip().split())
    ground = [[0]* M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    count = 0
    for j in range(K):
        x, y = map(int, input().rstrip().split())
        ground[y][x] = 1
    for row in range(N):
        for col in range(M):
            if ground[row][col] == 1 and visited[row][col] == 0:
                count += 1
                queue = deque()
                queue.append((col, row))
                while queue:
                    a, b = queue.popleft()
                    for m in range(4):
                        nx = a + mx[m]
                        ny = b + my[m]
                        if 0<= nx < M and 0 <= ny < N and ground[ny][nx] == 1 and visited[ny][nx] == 0:
                            queue.append((nx, ny))
                            visited[ny][nx] = 1
    print(count)