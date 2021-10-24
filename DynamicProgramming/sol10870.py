import sys

n = int(sys.stdin.readline().rstrip())

F = [0,1]

def sol(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(2,n+1):
            F.append(F[i-2]+F[i-1])
        return F[-1]

print(sol(n))
    