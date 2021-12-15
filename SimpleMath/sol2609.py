import sys

a, b = map(int, sys.stdin.readline().rstrip().split())

temp = max(a, b)
ans = []
for i in range(1, temp+1):
    if a % i ==0 and b % i == 0:
        ans.append(i)
    
GCD = ans[-1]
LCM = int((a*b)/GCD)

print(GCD)
print(LCM)