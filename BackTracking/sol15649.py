import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

answer = []
visited = [False] * (n+1)

def bt(num):
    if num == m:
        print(' '.join(map(str, answer)))
        return
    for i in range(1, n+1):
        if visited[i] == False:
            visited[i] = True
            answer.append(i)
            bt(num+1)
            visited[i] = False
            answer.pop()
    
bt(0)
