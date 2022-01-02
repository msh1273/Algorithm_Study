import sys

#마을, 벽, 돌
N, M, K = map(int, sys.stdin.readline().rstrip().split())

viliage = dict(enumerate(map(int, sys.stdin.readline().rstrip().split()),1))

rock = list(map(int, sys.stdin.readline().rstrip().split()))

mx = sum(viliage.values())

for i in rock:
    total = 0
    temp = 0
    for j in range(i, len(viliage)+1):
        temp += viliage[j]
    print(temp)
