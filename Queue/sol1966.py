import sys
from collections import deque

input = sys.stdin.readline

T = int(input().rstrip())

for i in range(T):
    n, m = map(int, input().rstrip().split())

    #문서의 가중치
    weight = deque()
    temp = list(map(int, input().rstrip().split()))
    weight.extend((i, val) for i, val in enumerate(temp))

    maxW = sorted(weight, key=lambda x : -x[1])[0][1]
    
    count = 1

    while weight:
        if weight[0][0] == m and weight[0][1] == maxW:
            print(count)
            break
        elif weight[0][1] == maxW:
            count += 1
            weight.popleft()
            maxW = sorted(weight, key=lambda x : -x[1])[0][1]
        else:
            weight.rotate(-1)


