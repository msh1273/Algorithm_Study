from sys import stdin

def dfs(i, result):
    global answer

    if i == len(op):
        answer = max(answer, int(result))
        return

    seq = str(eval(result + op[i] + number[i+1]))
    dfs(i+1, seq)

    if i+1 < len(op):
        bracket = str(eval(number[i+1] + op[i+1] + number[i+2]))
        bracket = str(eval(result + op[i] + bracket))
        dfs(i+2, bracket)

if __name__ == '__main__':
    n = int(stdin.readline())
    expression = stdin.readline()

    number = []
    op = []
    answer = -2**31
    for i in expression:
        if i.isdigit():
            number.append(i)
        else:
            op.append(i)
    op = op[:-1]
    dfs(0, number[0])
    print(answer)