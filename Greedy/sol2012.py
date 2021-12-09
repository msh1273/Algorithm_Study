import sys

n = int(sys.stdin.readline().rstrip())

rank = []
for i in range(n):
    rank.append(int(sys.stdin.readline().rstrip()))

rank.sort()

bulman = 0
for i in range(1, n+1):
    bulman += abs(i-rank[i-1])
print(bulman)