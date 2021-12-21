import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

li = deque()

for _ in range(n):
    cmd = sys.stdin.readline().rstrip().split()
    if cmd[0] == "push_front":
        li.appendleft(cmd[1])
    if cmd[0] == "push_back":
        li.append(cmd[1])
    if cmd[0] == "pop_front":
        if li:
            print(li.popleft())
        else:
            print(-1)
    if cmd[0] == "pop_back":
        if li:
            print(li.pop())
        else:
            print(-1)
    if cmd[0] == "size":
        print(len(li))
    if cmd[0] == "empty":
        if li:
            print(0)
        else:
            print(1)
    if cmd[0] == "front":
        if li:
            print(li[0])
        else:
            print(-1)
    if cmd[0] == "back":
        if li:
            print(li[-1])
        else:
            print(-1)