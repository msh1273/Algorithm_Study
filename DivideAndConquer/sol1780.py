import sys

N = int(sys.stdin.readline().rstrip())

a_1 = 0
a0 = 0
a1 = 0
paper = []
for i in range(N):
    paper.append(list(map(int, sys.stdin.readline().rstrip().split())))

def solve(row, col, N):
    global a_1, a0, a1
    cur = paper[row][col]
    for i in range(row, row+N):
        for j in range(col, col+N):
            if paper[i][j] != cur:  #같지 않으면 분할
                newN = N//3
                solve(row, col, newN)
                solve(row, col+newN, newN)
                solve(row, col+(2*newN), newN)
                solve(row+newN, col, newN)
                solve(row+newN, col+newN, newN)
                solve(row+newN, col+(2*newN), newN)
                solve(row+(2*newN), col, newN)
                solve(row+(2*newN), col+newN, newN)
                solve(row+(2*newN), col+(2*newN), newN)
                return
    if cur == -1:
        a_1 += 1
    elif cur == 0:
        a0 += 1
    else:
        a1 += 1
    return
solve(0,0,N)
print(a_1)
print(a0)
print(a1)