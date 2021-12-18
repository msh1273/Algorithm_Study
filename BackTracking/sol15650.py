import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

ans = []
def bt(num):
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return
    for i in range(num, n+1):
        ans.append(i)
        bt(i+1)
        ans.pop()
bt(1)