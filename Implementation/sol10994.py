n = int(input())

rule = 1 + 4*(n-1)

stars = [[' ' for _ in range(rule)] for _ in range(rule)]


def star(n, x, y):
    if n == 1:
        stars[y][x] = '*'
        return
    else:
        rule = 1 + 4*(n-1)
        for i in range(rule):
            stars[y][x+i] = '*'
            stars[y+i][x] = '*'
            stars[y + rule-1][x+i] = '*'
            stars[y + i][x+rule-1] = '*'
    star(n-1, x+2, y+2)

star(n, 0, 0)
for i in stars:
    print(''.join(i))