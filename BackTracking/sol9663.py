
n = int(input())

row = [0] * n
answer = 0

#현재 레벨에서 놓을 수 있는지 없는지 체크하는 함수 (행, 열, 대각선)
def can(level):
    for i in range(level):
        if row[level] == row[i] or abs(row[level] - row[i]) == level - i:
            return False
    return True


def dfs(level):
    global answer

    if level == n:
        answer += 1
        return
    else:
        for i in range(n):
            row[level] = i
            if can(level):
                dfs(level + 1)

dfs(0)
print(answer)