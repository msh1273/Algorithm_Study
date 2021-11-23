import sys
from itertools import combinations_with_replacement
n = int(sys.stdin.readline().rstrip())

roma = [1, 5, 10, 50]
temp = list(combinations_with_replacement(roma, n))
answer = []
for i in temp:
    if sum(i) not in answer:
        answer.append(sum(i))

print(len(answer))
