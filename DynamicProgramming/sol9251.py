import sys

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()

LCS = [[0]*(len(a)+1) for _ in range(len(b)+1)]
for i in range(1,len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            LCS[i][j] = LCS[i-1][j-1]+1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

print(a[0],b)
print(LCS[-1][-1])