n = int(input('몇글자?: '))
expression = input('수식 입력: ')

print(expression)

def cal (a, b, operator):
    if operator == "+":
        return a+b
    elif operator == "-":
        return a-b
    elif operator == "*":
        return a*b

if __name__ == '__main__':
    n = int(stdin.read)