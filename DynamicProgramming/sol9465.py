import sys

# 테스트 케이스 개수 t
t = int(sys.stdin.readline().rstrip())
answer = []

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    sticker = []
    for i in range(2):
        sticker.append(list(map(int, sys.stdin.readline().split())))
    for j in range(1, n):
        if j == 1:
            sticker[0][j] += sticker[1][j-1]
            sticker[1][j] += sticker[0][j-1]
        else:
            sticker[0][j] += max(sticker[1][j-1], sticker[1][j-2])
            sticker[1][j] += max(sticker[0][j-1], sticker[0][j-2])
    answer.append(max(sticker[0][n-1], sticker[1][n-1]))

for i in answer:
    print(i)
