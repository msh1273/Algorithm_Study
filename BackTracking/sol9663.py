
n = int(input())

row = [250] * n
answer = 0

#현재 레벨에서 놓을 수 있는지 없는지 체크하는 함수 (행[자동 생략], 열, 대각선)
def can(level):
    for i in range(level):
        if row[level] == row[i] or abs(row[level] - row[i]) == level - i:   #열위치가 같은 조건 | 열위치 차이와, 행위치 차이가 같다면 대각선
            return False
    return True


def dfs(level):
    global answer

    if level == n:
        answer += 1
        return
    else:
        for i in range(n):  #퀸을 배치할 열 
            row[level] = i  #퀸을 level행 i열에 배치
            if can(level):
                dfs(level + 1)

dfs(0)
print(answer)