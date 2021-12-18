import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

n_list = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

ans = []
visited = [False] * (n)

def bt(num):
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return
    for i in range(0,len(n_list)):
        if visited[i] == False:
            visited[i] = True
            ans.append(n_list[i])
            bt(num+1)
            visited[i] = False
            ans.pop()

bt(0)