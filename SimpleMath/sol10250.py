import sys
import math

input = sys.stdin.readline

n = int(input().rstrip())
for i in range(n):
    H, W, N = map(int, input().rstrip().split())

    width = math.ceil(N / H)
    if width < 10:
        width = "0" + str(width)
    else:
        width = str(width)

    height = 1
    if (N % H) == 0:
        height = H
    else:
        height = N % H
    
    print(str(height) + str(width))

    

