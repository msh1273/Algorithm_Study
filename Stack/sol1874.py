import abc
import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())


exInput = [int(input()) for _ in range(n)]

ans = []
for i in range(1, n+1):
    ans.append(i)

stack = []
maxN = 0

flag = True
answer = []
for i in exInput:
    if maxN == 0:
        for j in range(0, i):
            stack.append(ans[j])
            answer.append("+")
        stack.pop()
        answer.append("-")
        maxN = i
    else:
        if maxN < i:        #넣은 스택 어디까지인지 기록
            for j in range(maxN, i):
                stack.append(ans[j])
                answer.append("+")
            stack.pop()
            answer.append("-")
            maxN = i
        else:
            temp = stack.pop()
            if temp == i:
                answer.append("-")
            else:
                flag = False
                break

if flag:
    for i in answer:
        print(i)
else:
    print("NO")