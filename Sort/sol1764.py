import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

d = []
for i in range(n):
    d.append(sys.stdin.readline().rstrip())

b = []
for i in range(m):
    b.append(sys.stdin.readline().rstrip())

c = list(set(d) & set(b))
c.sort()

print(len(c))
for i in c:
    print(i)