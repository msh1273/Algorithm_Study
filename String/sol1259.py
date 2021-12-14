import sys

ans = []
input = sys.stdin.readline
while True:
    n = input().rstrip()
    if n == '0':
        break
    start = 0
    flag = True
    for i in range(len(n)//2):
        end = len(n)-1-start
        if n[start] != n[end]:
            ans.append("no")
            flag = False
            break
        else:
            start += 1
    if flag:
        ans.append("yes")

for i in ans:
    print(i)
