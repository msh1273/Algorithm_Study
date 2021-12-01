import sys

input = sys.stdin.readline().rstrip().split()
# 건물의 개수 n, 도로의 개수 m
n, m = map(int, input)

building = [i for i in range(n+1)]

print(building)
chicken1 = 0
chicken2 = 0

_map = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    _map[a-1][b-1] = _map[b-1][a-1] = 1

print(_map)
