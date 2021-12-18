import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

ans = []

def bt(num):
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return
    for i in range(num, n+1):
        ans.append(i)
        bt(i)
        ans.pop()
    
bt(1)