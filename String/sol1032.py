import sys
n = int(sys.stdin.readline().rstrip())

name = []

for i in range(n):
    temp = sys.stdin.readline().rstrip()
    name.append(temp)


temp = name[0]
answer = []
for i in range(len(temp)):
    answer.append(temp[i])
    for j in range(n):
        if temp[i] != name[j][i]:
            answer[i] = '?'
            break
print(''.join(answer))