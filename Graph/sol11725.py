import sys
sys.setrecursionlimit(10**9)

n = int(sys.stdin.readline().rstrip())

tree = [[] for i in range(n+1)]
parent = [0 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(node):
    for i in tree[node]:
        if parent[i] == 0:
            parent[i] = node
            dfs(i)

dfs(1)

parent = parent[2:]
for i in parent:
    print(i)