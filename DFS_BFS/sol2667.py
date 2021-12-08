import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline().rstrip())

# 지도 입력
graph = []
for i in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip()))
    graph.append(temp)

#단지 체크
visited = [[0 for _ in range(n)] for _ in range(n)]

#상 하 좌 우
mx = [-1, 1, 0 , 0]
my = [0, 0, -1, 1]

stack = []
count = 0
def dfs(x, y, stack):
    visited[x][y] = 1
    stack.append((x,y))
    for i in range(4):
        nx = x + mx[i]
        ny = y + my[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1 and visited[nx][ny] == 0:
            dfs(nx, ny, stack)
    return len(stack)

answer = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 0 and visited[i][j] == 0:
            visited[i][j] = 1
        elif graph[i][j] == 1 and visited[i][j] == 0:
            stack = []
            answer.append(dfs(i, j, stack))

answer.sort()
print(len(answer))
for i in answer:
    print(i)
