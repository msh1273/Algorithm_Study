import sys
from collections import deque

# 보드의 행: n 보드의 열: m
n, m = map(int, sys.stdin.readline().split())

# 격자판 생성
board = []

for row in range(0, n):
    board.append(list(map(int, sys.stdin.readline().split())))

# 마지막줄 입력 직사각형의 크기 H * W, 시작 좌표 Sr, Sc, 도착 좌표 Fr, Fc
H, W, Sr, Sc, Fr, Fc = map(int, sys.stdin.readline().split())

# 좌표 시작 기준점이 1,1 이므로 1씩 빼준다.
Sr, Sc, Fr, Fc = Sr-1, Sc-1, Fr-1, Fc-1

# 직사각형이 움직일 수 있는 방향 (왼, 오, 위, 아래)
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 방문했던 곳인지 체크
visited = [[0 for i in range(m)] for _ in range(n)]


# 움직였는데 직사각형이 벽(1)과 충돌이 있는지 판별하는 함수
def isMove(curPoint):
    if curPoint[0] >= n-H+1 or curPoint[1] >= m-W+1:
        return False
    for row in range(H):
        for col in range(W):
            if curPoint[0]+row < 0 or curPoint[0]+row > n or curPoint[1]+col < 0 or curPoint[1]+col > m or board[curPoint[0]+row][curPoint[1]+col] == 1:
                return False
    return True


def bfs():
    queue = deque()
    queue.append((0, Sr, Sc))
    while queue:
        count, qrow, qcol = queue.popleft()

        # 종료 조건
        if qrow == Fr and qcol == Fc:
            return count

        for mrow, mcol in moves:
            curPoint = (qrow+mrow, qcol+mcol)
            if 0 <= curPoint[0] <= n-1 and 0 <= curPoint[1] <= m-1 and isMove(curPoint) and not visited[curPoint[0]][curPoint[1]]:
                visited[curPoint[0]][curPoint[1]] = 1
                queue.append((count+1, curPoint[0], curPoint[1]))
    return -1


print(bfs())
