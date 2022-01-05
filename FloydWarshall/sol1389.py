import sys

# N유저의 수, M관계의 수
N, M = map(int, sys.stdin.readline().rstrip().split())

rel = [[0] * (N) for _ in range(N)]
<<<<<<< HEAD

# 그래프 만들기(자기 자신에게 가는 경우는 모두 0 나머지는 inf
=======
>>>>>>> master
for i in range(N):
    for j in range(N):
        if i == j:
            rel[i][j] = 0
        else:
            rel[i][j] = float('inf')

<<<<<<< HEAD
# 경로가 이어진 곳 1로 만드는 작업
=======
>>>>>>> master
for i in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    rel[a-1][b-1] = rel[b-1][a-1] = 1

<<<<<<< HEAD

# 플로이드 와샬
for k in range(N):
=======
for k in range(N):
    score = 0
>>>>>>> master
    for i in range(N):
        for j in range(N):
            rel[i][j] = min(rel[i][j], rel[i][k]+rel[k][j])

<<<<<<< HEAD
# dict로 만들어서 value로 오름차순 정렬하기
=======
>>>>>>> master
answer = []
for i in rel:
    answer.append(sum(i))
answer = sorted(dict(enumerate(answer)).items(), key=lambda x: x[1])
print(answer[0][0] + 1)