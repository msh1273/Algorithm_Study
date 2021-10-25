import sys

T = int(sys.stdin.readline().rstrip())
answer = []

for i in range(T):
    A = [1, 2, 4]
    n = int(sys.stdin.readline().rstrip())
    if n >= 3:
        for j in range(3, n):
            A.append(A[j-3]+A[j-2]+A[j-1])
        answer.append(A[-1])
    else:
        answer.append(A[n-1])

for i in answer:
    print(i)