import sys

input = sys.stdin.readline

n = int(input().rstrip())

stack = []
for i in range(n):
    st = input().rstrip().split()
    if len(st) == 2 and st[0] == 'push':
        stack.append(int(st[1]))
    if st[0] == 'pop':
        if stack:
            print(stack[-1])
            stack.pop()
        else:
            print(-1)
    if st[0] == 'size':
        print(len(stack))
    if st[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    if st[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
