import sys

def dfs(node, dist, cnt):
    global N, weights, visited, shortest
    
    # N개 노드 모두 방문했으면 시작점으로 되돌아가기
    if cnt == N:
        if weights[node][0] > 0:
            shortest = min(shortest, dist + weights[node][0])
        return
    # 이웃한 노드 중 방문하지 않은 노드 방문
    for idx, w in enumerate(weights[node]):
        if w > 0 and not visited[idx]:
            visited[idx] = 1
            dfs(idx, dist+w, cnt+1)
            visited[idx] = 0

if __name__ == '__main__':
    N = int(input())
    weights = []
    visited = [0 for _ in range(N)]
    shortest = float('inf')
    for _ in range(N):
        weights.append(list(map(int, input().split())))

    visited[0] = 1
    dfs(0, 0, 1)
    print(shortest)