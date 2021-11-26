import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().rstrip().split())

graph = [i for i in range(n+1)]


def findParent(n):
    if graph[n] == n:
        return n
    graph[n] = findParent(graph[n])
    return graph[n]


def union(graph, a, b):
    a = findParent(a)
    b = findParent(b)
    if a < b:
        graph[b] = a
    else:
        graph[a] = b


answer = []

for _ in range(m):
    check, a, b = map(int, sys.stdin.readline().rstrip().split())
    if check == 1:
        if findParent(a) == findParent(b):
            answer.append("YES")
        else:
            answer.append("NO")
    else:
        union(graph, a, b)

for i in answer:
    print(i)
