import sys

def dfs(city, val, count):
    global n, graph, visited, path
    
    # N개 노드 모두 방문했으면 시작점으로 되돌아가기
    if count == n:
        if graph[city][0] > 0:
            path = min(path, val + graph[city][0])
        return
        
    for i, w in enumerate(graph[city]):
        # 도로가 있고, 방문하지 않은 도시인 경우
        if w > 0 and not visited[i]:
            visited[i] = 1
            dfs(i, val+w, count+1)
            visited[i] = 0

if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    graph = []
    visited = [0] * n
    path = float('inf')

    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

    visited[0] = 1
    dfs(0, 0, 1)
    print(path)