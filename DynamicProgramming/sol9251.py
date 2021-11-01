import sys

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()

LCS = [[0]*(len(b)+1) for _ in range(len(a)+1)]
for i in range(0,len(a)+1):
    for j in range(0, len(b)+1):
        if i == 0 or j == 0:
            LCS[i][j] == 0
        elif a[i-1] == b[j-1]:
            LCS[i][j] = LCS[i-1][j-1]+1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

print(LCS[-1][-1])