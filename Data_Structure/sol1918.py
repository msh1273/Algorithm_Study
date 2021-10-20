import sys
exp = sys.stdin.readline().rstrip()

# (A+(B*C)) - (D/E)
priority = {
    '(' : 1,
    '+' : 2, '-' : 2,
    '*' : 3, '/' : 3
}

operand = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
stack = []
result = []
ans = ''
for i in exp:
    if i in operand:    #피 연산자인 경우
        result.append(i)
    elif i == '(':
        stack.append(i)
    elif i == ')':
        while stack and stack[-1] != '(':
            result.append(stack.pop())
        stack.pop() # (을 빼는 역할
    else:   # 연산자인 경우
        while stack and priority[i] <= priority[stack[-1]]:
            result.append(stack.pop())
        stack.append(i)
while stack:
    result.append(stack.pop())

for i in result:
    ans += i
    
print(ans)