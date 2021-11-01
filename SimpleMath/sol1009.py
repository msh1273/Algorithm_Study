import sys

T = int(sys.stdin.readline().rstrip())
answer = []
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    b = b%4
    if b%4 ==0 :
        b = 4
    s = a**b
    if s%10 == 0:
        answer.append(10)
    else:
        answer.append(s%10)

for i in answer:
    print(i)