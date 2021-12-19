import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

n_list = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

ans = []

def bt(num):
    if len(ans) == m:
        print(' '.join(map(str,ans)))
        return
    for i in range(num, len(n_list)):
        ans.append(n_list[i])
        bt(i+1)
        ans.pop()

bt(0)