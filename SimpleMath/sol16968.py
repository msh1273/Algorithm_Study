import sys

n = list(sys.stdin.readline().rstrip())

answer = 1

if n[0] == 'd':
    answer = 10
else:
    answer = 26

for i in range(1, len(n)):
    if n[i] == 'd':
        if n[i-1] == 'd':
            answer *= 9
        else:
            answer *= 10
    else:
        if n[i] == 'c':
            if n[i-1] == 'c':
                answer *= 25
            else:
                answer *= 26


print(answer)
