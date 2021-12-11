import sys

n = sys.stdin.readline().rstrip().split('-')

ans = []
for i in range(len(n)):
    temp = n[i].split('+')
    _sum = 0
    for j in temp:
        j = int(j)
        _sum += j
    ans.append(_sum)

answer = ans[0]
if len(ans) == 1:
    print(answer)
else:   
    for i in range(1, len(ans)):
        answer -= ans[i]
    print(answer)