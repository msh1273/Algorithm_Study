import sys

N = int(sys.stdin.readline().rstrip())
answer = []
# 회의 시간이 짧은 순서대로 정렬한다.
for i in range(N):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    answer.append([a, b])

answer.sort(key=lambda x: (x[1], x[0]))

count = 1
now = answer[0][1]
for i in range(1, N):
    if answer[i][0] >= now:
        count += 1
        now = answer[i][1]

print(count)
