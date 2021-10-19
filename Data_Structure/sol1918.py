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
for i in exp:
    if i in operand:
        result.append(i)
    elif i == '(':
        stack.append(i)
    elif i == ')':
        while stack and stack[-1] != '(':
            result.append(stack.pop())
        stack.pop()
    else:
        while stack and priority[i] <= priority[stack[-1]]:
            result.append(stack.pop())
        stack.append(i)
print(stack)