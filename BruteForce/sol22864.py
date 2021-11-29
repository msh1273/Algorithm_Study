import sys

# 피로도는 0보다 작아질 수 없다. (1시간일하면 A만큼 피로도 쌓이고 B만큼 처리가능) 1시간 쉬면 C만큼 피로도 줄어듬 처리한 일은 0
# 피로도 M넘으면 번아웃

p = 0
value = 0

A, B, C, M = map(int, sys.stdin.readline().rstrip().split())

for i in range(24):
    if p+A <= M:
        p = p+A
        value += B
    else:
        if p-C >= 0:
            p = p-C
        else:
            p = 0

print(value)
