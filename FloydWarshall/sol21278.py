import sys

input = sys.stdin.readline().rstrip().split()
# 건물의 개수 n, 도로의 개수 m
n, m = map(int, input)

chicken1 = 0
chicken2 = 0

_map = [[float('inf') for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            _map[i][j] = 0
        else:
            _map[i][j] = float('inf')

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    _map[a-1][b-1] = _map[b-1][a-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            _map[i][j] = min(_map[i][j], _map[i][k] + _map[k][j])

count = 0
answer = []
for i in range(n):
    for j in range(n):
        count = 0
        chicken1 = i
        chicken2 = j
        if chicken1 != chicken2:
            for k in range(n):
                if k != chicken1 and k != chicken2:
                    count += min(_map[k][chicken1], _map[k][chicken2])
        else:
            continue
        count *= 2
        answer.append((i,j, count))

answer = sorted(answer, key = lambda x: (x[2], x[0], x[1]))

c1 = answer[0][0]+1
c2 = answer[0][1]+1
s = answer[0][2]

if c1 < c2:
    print(c1, c2, s)
else:
    print(c2, c1, s)