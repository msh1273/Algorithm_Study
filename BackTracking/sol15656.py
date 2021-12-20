import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

n_list = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

answer = []

def bt(num):
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return
    for i in range(len(n_list)):
        answer.append(n_list[i])
        bt(i)
        answer.pop()

bt(0)