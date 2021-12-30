import sys

n = int(sys.stdin.readline().rstrip())

result = 1
for i in range(n, 0, -1):
    result *= i

ans = 0
result = list(str(result))
while result:
    if result[-1] == '0':
        ans += 1
        result.pop()
    else:
        break

print(ans)