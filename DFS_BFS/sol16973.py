import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

# 격자판 생성
board = []

for row in range(0, n):
    board.append(sys.stdin.readline().split())

# 마지막줄 입력 직사각형의 크기 H, W, 시작 좌표 Sr, Sc, 도착 좌표 Fr, Fc
H, W, Sr, Sc, Fr, Fc = map(int, sys.stdin.readline().split())

# 직사각형이 움직일 수 있는 방향 (왼, 오, 위, 아래)
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

startPoint = (Sr-1, Sc-1)
endPoint = (Fr-1, Fc-1)

# 움직였는데 직사각형이 벽(1)과 충돌이 있는지 판별하는 함수


def isMove(board, curPoint, H, W):
    for i in range(0, H):
        for j in range(0, W):
            if 0 < curPoint[0]+i < n and 0 < curPoint[1]+j < m and board[curPoint[0]+i][curPoint[1]+j] == 1:
                return False
    return True


count = -1
queue = deque()
queue.append((Sr-1, Sc-1))
while queue:
    curPoint = queue.popleft()
    count += 1
    # 종료 조건
    if curPoint[0] == Fr and curPoint[1] == Fc:
        break
    for x, y in moves:
        temp = (curPoint[0]+x, curPoint[1]+y)
        if 0 <= temp[0] <= n-1 and 0 <= temp[1] <= m-1:
            if isMove(board, temp, H, W):  # 움직일 수있는 곳이 있는 경우
                queue.append(temp)
            else:  # 더이상 상하좌우로 움직일 수 없음
                count = 0

print(count)
