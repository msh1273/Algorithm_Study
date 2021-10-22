import sys
from collections import deque

chess = []

currentPoint = (7,0)
move = [(0,0), (1,0),(-1,0),(0,-1),(0,1), (1,-1),(1,1),(-1,-1),(-1,1)] #제자리, 상,하,좌,우, 대(상좌),대(상우),대(하좌),대(하우)

# 체스판 상태 입력
for i in range(8):
    chess.append(list(sys.stdin.readline().rstrip()))

# moveWall이 호출되면 벽이 1칸씩 내려옴
def moveWall(chess):
    a = '........'
    chess.insert(0, list(a))
    chess.pop()
    return chess

def bfs(chess, currentPoint):
    queue = deque()
    queue.append(currentPoint)
    while queue:
        temp = queue.popleft()
        for i in move:
            currentPoint = temp
            movePoint = tuple(sum(elem) for elem in zip(currentPoint, i))
            if movePoint[0] <= 7 and movePoint[0] >= 0 and movePoint[1] <= 7 and movePoint[1] >= 0:
                if chess[movePoint[0]][movePoint[1]] != '#' and chess[movePoint[0]-1][movePoint[1]] != '#':
                    if movePoint[0] == 0:
                        print(queue)
                        return 1
                    queue.append(movePoint)
        moveWall(chess)
    return 0

print(bfs(chess, currentPoint))