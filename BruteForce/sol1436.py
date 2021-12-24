import sys

input = sys.stdin.readline

num = 666
n = int(input().rstrip())

while n != 0:
    if "666" in str(num):
        n -= 1
        if n == 0:
            break
    num += 1

print(num)