import sys

t = int(sys.stdin.readline().rstrip())
answer = []

for i in range(t):
    quest = list(map(str, sys.stdin.readline().rstrip()))
    stack = []
    flag = True
    for i in quest:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                flag = False
                break
    if stack:
        flag = False

    if flag == True:
        answer.append("YES")
    else:
        answer.append("NO")

for i in answer:
    print(i)