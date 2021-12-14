import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

board = []
for i in range(n):
    board.append(input().rstrip())

ans = []
for i in range(n-7): 
    for j in range(m-7):
        firstWhite = 0
        firstBlack = 0
        for a in range(i, 8+i):
            for b in range(j, 8+j):
                if (a+b) % 2 == 0:
                    if board[a][b] != "W":
                        firstWhite += 1
                    if board[a][b] != "B":
                        firstBlack += 1
                else:
                    if board[a][b] != "B":
                        firstWhite += 1
                    if board[a][b] != "W":
                        firstBlack += 1
        ans.append(min(firstWhite, firstBlack))
print(min(ans))
