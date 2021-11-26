import sys

# 점의 개수 n, 차례의 수 m
n, m = map(int, sys.stdin.readline().rstrip().split())

dot = [i for i in range(n)]

graph = []


def find(node):
    if dot[node] == node:
        return node
    else:
        dot[node] = find(dot[node])
    return dot[node]


def union(dot, a, b):
    a = find(a)
    b = find(b)
    if a < b:
        dot[b] = a
    else:
        dot[a] = b


for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph.append([a, b])


def ans(graph):
    count = 0
    for a, b in graph:
        if find(dot[a]) == find(dot[b]):  # 부모 노드가 같다는 것은 사이클이 생긴다는 의미
            return count+1
        union(dot, a, b)
        count += 1
    return 0


print(ans(graph))
