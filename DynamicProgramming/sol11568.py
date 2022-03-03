import sys

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().rstrip().split()))
dp = [1] * N

first = arr[0]

for i in range(1, N):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
