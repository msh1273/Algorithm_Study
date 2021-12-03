import sys

input = sys.stdin.readline

n = int(input().rstrip())

weight = []
weight = list(map(int, input().rstrip().split()))
weight.sort()

answer = 0
for i in weight:
    if i > answer+1:
        break
    answer += i
print(answer+1)
    