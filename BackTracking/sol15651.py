import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

ans = []

def bt(num):
    if num == m:
        print(' '.join(map(str, ans)))
        return
    for i in range(1, n+1):
        ans.append(i)
        bt(num+1)
        ans.pop()
    
bt(0)