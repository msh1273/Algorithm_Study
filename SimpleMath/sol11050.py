import sys
import math

n, k = map(int, sys.stdin.readline().rstrip().split())

answer = math.factorial(n) / (math.factorial(k) * math.factorial((n-k)))
print(int(answer))