import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

a = input().rstrip().split()
b = input().rstrip().split()

ans = list(map(int,a+b))
ans = sorted(ans)

print(*ans)