import sys

T = int(sys.stdin.readline().rstrip())

answer = []
for i in range(T):
    denominator = 1
    numerator = 1
    N, M = map(int,sys.stdin.readline().split())
    
    for i in range(N):
        denominator *= M
        M -= 1

    temp = N

    for i in range(N):
        numerator *= temp
        temp -= 1

    answer.append(denominator//numerator)

for i in answer:
    print(i)