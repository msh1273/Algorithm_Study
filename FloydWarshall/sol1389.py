import sys

# N유저의 수, M관계의 수
N, M = map(int, sys.stdin.readline().rstrip().split())

rel = [[0] * (N) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            rel[i][j] = 0
        else:
            rel[i][j] = float('inf')

for i in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    rel[a-1][b-1] = rel[b-1][a-1] = 1

for k in range(N):
    score = 0
    for i in range(N):
        for j in range(N):
            rel[i][j] = min(rel[i][j], rel[i][k]+rel[k][j])

answer = []
for i in rel:
    answer.append(sum(i))
answer = sorted(dict(enumerate(answer)).items(), key=lambda x: x[1])
print(answer[0][0] + 1)