import sys

chess = []

start_low = 7
start_col = 0
# 체스판 상태 입력
for i in range(8):
    chess.append(list(sys.stdin.readline().rstrip()))

print(chess[0][0])