import sys
sys.setrecursionlimit(10**6)
# n: 도시의 수, m: 여행 계획에 속한 도시의 수
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

parent = [i for i in range(n)]


def union(i, j):
    i = find(i)
    j = find(j)
    if i < j:
        parent[j] = i
    else:
        parent[i] = j


def find(n):
    if parent[n] == n:
        return n
    parent[n] = find(parent[n])
    return parent[n]


graph = []
for i in range(n):
    graph = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(len(graph)):
        if graph[j] == 1:
            union(parent[i], parent[j])

que = []
que = list(map(int, sys.stdin.readline().rstrip().split()))
for i in range(len(que)):
    que[i] -= 1

temp = find(que[0])


def answer(que, temp):
    for i in range(len(que)):
        if find(que[i]) != temp:
            return "NO"
    return "YES"


print(answer(que, temp))
