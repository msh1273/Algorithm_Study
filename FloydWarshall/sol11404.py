import sys
input = sys.stdin.readline

# n 도시의 개수, m 버스의 개수
n = int(input().rstrip())
m = int(input().rstrip())

graph = [[float('inf') for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] = 0

for i in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in graph:
    for j in i:
        print(j, end=' ')
    print()