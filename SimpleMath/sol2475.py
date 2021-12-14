import sys

num = list(map(int, sys.stdin.readline().rstrip().split()))
s = [i*i for i in num]
ans = sum(s) % 10
print(ans)