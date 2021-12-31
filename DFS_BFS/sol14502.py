import sys
import copy
from collections import deque
from itertools import combinations

n, m = map(int, sys.stdin.readline().rstrip().split())

lab = []
visited = [[False] * m for _ in range(n)]
for i in range(n):
    lab.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 상, 하, 좌, 우
mx = [-1,1,0,0]
my = [0,0,-1,1]

canWall = []
for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            canWall.append((i,j))

wa = list(combinations(canWall, 3))

def bfs(temp, row, col):
    queue = deque()
    queue.append((row,col))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nrow = x + mx[i]
            ncol = y + my[i]
            if 0 <= nrow < n and 0 <= ncol < m and temp[nrow][ncol] == 0:
                queue.append((nrow, ncol))
                temp[nrow][ncol] = 2
    return temp

answer = []

for i in wa:        #연구실 벽 초기화
    temp = copy.deepcopy(lab)
    count = 0
    for x, y in i:
        temp[x][y] = 1
    for row in range(n):
        for col in range(m):
            if temp[row][col] == 2:
                temp = bfs(temp, row, col)

    for row in range(n):
        for col in range(m):
            if temp[row][col] == 0:
                count += 1
    answer.append(count)
print(max(answer))
