import sys

# n은 행, m은 열
n, m = map(int, sys.stdin.readline().rstrip().split())

count = 0
answer = []

board = []
for i in range(n):
    board.append(list(sys.stdin.readline().rstrip()))

# 사용된 별인지 체크하기 위한 리스트
visited = [[0 for _ in range(m)] for _ in range(n)]

# 1인 곳은 별이 아직 사용 되지 않음.
for i in range(n):
    for j in range(m):
        if board[i][j] == '*':
            visited[i][j] = 1


def checkStarCount(i, j, size, visited):
    count = 0
    answer = []
    for s in range(1, size+1):
        if board[i-s][j] == '*' and board[i+s][j] == '*' and board[i][j-s] == '*' and board[i][j+s] == '*':
            count = 1
            answer = [i+1, j+1, s]
            visited[i][j] = 0
            visited[i-s][j] = 0
            visited[i+s][j] = 0
            visited[i][j-s] = 0
            visited[i][j+s] = 0
        else:
            return 1, answer
    return count, answer


for i in range(1, n-1):
    for j in range(1, m-1):
        # 중앙에 *인지 확인
        if board[i][j] == '*':
            # 가능한 최대 사이즈
            size = min(i, n-i-1, j, m-j-1)
            Acount, Aanswer = checkStarCount(i, j, size, visited)
            if Aanswer:
                answer.append(Aanswer)
                count += Acount

_sum = 0
for i in visited:
    _sum += sum(i)

if _sum == 0:
    # 정상 수행
    print(count)
    for i in answer:
        print(i[0], i[1], i[2])
else:
    print(-1)
